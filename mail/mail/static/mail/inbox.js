document.addEventListener('DOMContentLoaded', function() {
	// Use buttons to toggle between views
	document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
	document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
	document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
	document.querySelector('#compose').addEventListener('click', compose_email);

	// By default, load the inbox
	load_mailbox('inbox');
});

function compose_email() {
	// Show compose view and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#email-display-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'block';

	// Clear out composition fields
	document.querySelector('#compose-recipients').value = '';
	document.querySelector('#compose-subject').value = '';
	document.querySelector('#compose-body').value = '';

	//Add submit function for form
	document.querySelector('#compose-form').onsubmit = sendEmail;

	//Submit function - sends email
	function sendEmail(event) {
		console.log('Sent email');
		fetch('/emails', {
			method: 'POST',
			body: JSON.stringify({
				recipients: document.getElementById('compose-recipients').value,
				subject: document.getElementById('compose-subject').value,
				body: document.getElementById('compose-body').value
			})
		})
			.then((response) => response.json())
			.then((result) => {
				// Print result
				console.log(result);
			});
		//Load sent mailbox
		document.getElementById('sent').click();
		return false;
	}
}

function load_mailbox(mailbox) {
	console.log('Loading');
	// Show the mailbox and hide other views
	document.querySelector('#emails-view').style.display = 'block';
	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-display-view').style.display = 'none';

	// Show the mailbox name
	document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

	fetch(`/emails/${mailbox}`).then((response) => response.json()).then(createEmailTable);

	function createEmailTable(emails) {
		// Print emails
		console.log(emails);

		//Create a table with headings
		const table = document.createElement('table');
		let thead = table.createTHead();
		let tbody = table.createTBody();

		let headerRow = thead.insertRow();
		for (let header of [ 'Sender', 'Subject', 'Timestamp' ]) {
			let th = document.createElement('th');
			th.innerHTML = header;
			headerRow.appendChild(th);
		}

		//Populate rows of table
		for (let email of emails) {
			let row = tbody.insertRow();
			for (let key of [ 'sender', 'subject', 'timestamp' ]) {
				let cell = row.insertCell();
				let text = document.createTextNode(email[key]);
				cell.appendChild(text);
			}
			//If this email has been read
			if (email.read) {
				row.classList.add('read');
			}

			//Bound function that passes the email object to load_email_view

			//Add an onclick function to load_email_view
			row.addEventListener('click', load_email.bind({ email }));
		}
		//Add table to emails view
		document.querySelector('#emails-view').appendChild(table);
		console.log('Added the table');
	}
}

function load_email() {
	// Show the email-display-view and hide other views
	document.querySelector('#emails-view').style.display = 'none';
	document.querySelector('#compose-view').style.display = 'none';
	document.querySelector('#email-display-view').style.display = 'grid';

	//Get rid of any leftover innerHTML
	document.querySelector('#email-display-view').innerHTML = '';

	//Create email info container
	let emailInfo = document.createElement('div');
	emailInfo.classList.add('info-cont');
	//Create email body container
	let emailBody = document.createElement('div');
	emailBody.classList.add('body-cont');
	//Create buttons container
	let buttonCont = document.createElement('div');
	buttonCont.classList.add('button-cont');

	//create sender info
	let sender = document.createElement('h6');
	sender.classList.add('sender');
	sender.innerHTML = `Sender: ${this.email.sender}`;

	//Add recipient info
	let recipient = document.createElement('h6');
	recipient.classList.add('recipient');
	recipients = this.email.recipients.join(',');
	recipient.innerHTML = `Recipient: ${recipients}`;

	//Add Timestamp info
	let timestamp = document.createElement('h6');
	timestamp.classList.add('timestamp');
	timestamp.innerHTML = `Timestamp: ${this.email.timestamp}`;

	//Add all to emailInfo
	emailInfo.append(sender, recipient, timestamp);

	//Add body content
	emailBody.innerHTML = this.email['body'];

	function createButton(text, className = '', onClick = null) {
		/* 
      Args: 
        text (str) used as name of button
        className (str) classname of button (defaults to "")
        onclick (function) used for onclick function defaults to none

      returns: 
        Button element
    */
		const button = document.createElement('button');
		if (className) {
			button.className = className;
		}
		button.innerHTML = text;
		button.addEventListener('click', onClick);
		return button;
	}
	function reverseArchiveEmail() {
		/* 
      Changes the archive boolean value of email to opposite of what it currently is
      Args:
        context: this should be an email object

      Sends a put request and archives the email
      Then loads user's inbox
    */
		fetch(`/emails/${this.id}`, {
			method: 'PUT',
			body: JSON.stringify({
				archived: !this.archived
			})
		});

		//Load the user's inbox
		load_mailbox('inbox');
	}
	//Create bound reverseArchiveEmail
	let boundArchive = reverseArchiveEmail.bind(this.email);
	if (this.email.archived) {
		//If archived add button to unarchive
		archiveButton = createButton('Unarchive', 'btn btn-sm btn-outline-primary', boundArchive);
	} else {
		//else add button to archive
		archiveButton = createButton('Archive', 'btn btn-sm btn-outline-primary', boundArchive);
	}
	//Add archive button to buttonCont
	buttonCont.appendChild(archiveButton);

	function replyToEmail() {
		/* 
      loads the email composition form and prefills certain boxes
      Args:
        context: this should be an email object

      returns: undefined

    */
		//Display the compose email div
		compose_email();
		console.log(this);
		//Fill in fields
		document.querySelector('#compose-recipients').value = this.recipients.join(' ');

		//Format subject
		if (this.subject.slice(0, 3) !== 'Re:') {
			//Add "Re:" if it doesn't already exist
			subject = `Re: ${this.subject}`;
		} else {
			subject = this.subject;
		}
		document.querySelector('#compose-subject').value = subject;
		document.querySelector('#compose-body').value = `On ${this.timestamp} ${this.sender} wrote: \n ${this.body}`;
	}
	let boundEmail = replyToEmail.bind(this.email);
	//Create reply button
	replyButton = createButton('Reply', 'btn btn-sm btn-outline-primary', boundEmail);

	//Add archive button to buttonCont
	buttonCont.appendChild(replyButton);

	//Add emailInfo, buttonCont and emailBody to the DOM
	document.querySelector('#email-display-view').append(emailInfo, emailBody, buttonCont);

	//Update the email to read
	fetch(`/emails/${this.email.id}`, {
		method: 'PUT',
		body: JSON.stringify({
			read: true
		})
	});
}
