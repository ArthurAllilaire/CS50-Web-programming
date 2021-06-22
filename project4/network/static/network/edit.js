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
	console.log(text);

	//Add the initial information to the form
	form.querySelector('#id_text').value = text;

	//Add submit function for form
	form.onsubmit = sendPost;

	function sendPost(event) {
		console.log('works');
		return false;
		fetch('/edit-post', {
			method: 'POST',
			body: JSON.stringify({
				text: document.getElementById('id_text').value
			})
		});
	}
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
		console.log('works');

		//Get form and hide it
		const form = post.querySelector('form');
		//Make it hidden
		form.setAttribute('hidden', true);

		//Get text
		const text = post.querySelector('.text');
		text.style.display = 'block';
	}
});
