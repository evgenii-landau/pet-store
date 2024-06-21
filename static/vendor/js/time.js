// Time for messages
document.addEventListener('DOMContentLoaded', function() {
	setTimeout(function() {
		let messages = document.querySelectorAll('.alert');
		messages.forEach(function(message) {
			message.style.display = 'none';
		});
	}, 3000);
});