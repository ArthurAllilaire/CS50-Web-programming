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

	// Show the mailbox name
	document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

	fetch(`/emails/${mailbox}`).then((response) => response.json()).then(createEmailTable);

	function createEmailTable(emails) {
		// Print emails
		console.log(emails);
		const table = document.createElement('table');
		//Create a table with headings
		let thead = table.createTHead();
		let row = thead.insertRow();
		for (let header of [ 'Sender', 'Subject', 'Timestamp' ]) {
			let th = document.createElement('th');
			th.innerHTML = header;
			row.appendChild(th);
		}

		//Populate rows of table
		for (let email of emails) {
			let row = table.insertRow();
			for (let key of [ 'sender', 'subject', 'timestamp' ]) {
				let cell = row.insertCell();
				let text = document.createTextNode(email[key]);
				cell.appendChild(text);
			}
		}
		//Add table to emails view
		document.querySelector('#emails-view').appendChild(table);
		console.log('Added the table');
	}
}
