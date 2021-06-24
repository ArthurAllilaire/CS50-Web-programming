function showFormNotText(post) {
	/* Takes a post element */
	//Replace text with prepopulated form of text
	const textCont = post.querySelector('.text');
	const text = textCont.innerHTML;
	//Hide the text content
	textCont.style.display = 'none';

	//Show the form which is added by django backend
	const form = post.querySelector('.edit-form');
	form.removeAttribute('hidden');

	//Add the initial information to the form
	form.querySelector('#id_text').value = text;

	function sendPost(event) {
		//Hide form and show text
		event.preventDefault();
		const post = this.parentElement;
		const textValue = this.querySelector('#id_text').value;
		const text = post.querySelector('.text');
		text.innerHTML = textValue;
		text.style.display = 'block';

		this.setAttribute('hidden', true);

		// Trying to send a post method, so need to have csrf token
		csrftoken = this.querySelector('input[name=csrfmiddlewaretoken]').value;

		//Create a request with the csrf token
		const request = new Request('/edit-post', { headers: { 'X-CSRFToken': csrftoken } });

		//Pass the request and body of form
		fetch(request, {
			method: 'POST',
			mode: 'same-origin',
			body: JSON.stringify({
				text: textValue,
				pk: this.querySelector('.pk').value
			})
		})
			.then((response) => response.json())
			.then((result) => {
				// Print result
				console.log(result);
			});
	}
	let boundSendPost = sendPost.bind(form);

	//Add submit function for form
	form.addEventListener('submit', boundSendPost, true);
}

document.addEventListener('click', function(event) {
	// Run edit posts, making all edit buttons functional
	const element = event.target;

	// Check if the edit button was pressed
	if (element.classList.contains('edit-btn')) {
		//Get post (first parent element is the header)
		const post = element.parentElement.parentElement;

		//Then show form and remove text
		showFormNotText(post);
	} else if (element.classList.contains('cancel-btn')) {
		const post = element.parentElement.parentElement.parentElement;

		//Get form and hide it
		const form = post.querySelector('form');
		//Make it hidden
		form.setAttribute('hidden', true);

		//Get text
		const text = post.querySelector('.text');
		text.style.display = 'block';
	}
});
