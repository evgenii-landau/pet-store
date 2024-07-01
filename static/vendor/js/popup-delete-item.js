// document.addEventListener('DOMContentLoaded', function () {
// var deleteModal = document.getElementById('deleteModal');
// var confirmDeleteButton = document.getElementById('confirmDeleteButton');
// var cancelDeleteButton = document.getElementById('cancelDeleteButton');
// var itemId;

// document.querySelectorAll('.remove-from-basket').forEach(function(button) {
// button.addEventListener('click', function () {
// 	itemId = button.getAttribute('data-item-id');
// 	deleteModal.style.display = 'block';
// });
// });

// cancelDeleteButton.addEventListener('click', function () {
// deleteModal.style.display = 'none';
// });

// window.addEventListener('click', function(event) {
// if (event.target == deleteModal) {
// 	deleteModal.style.display = 'none';
// }
// });

// confirmDeleteButton.addEventListener('click', function () {
// fetch(`{% url 'delete_basket_item' 0 %}`.replace('0', itemId), {
// 	method: 'POST',
// 	headers: {
// 		'X-CSRFToken': '{{ csrf_token }}'
// 	}
// })
// .then(response => {
// 	if (response.ok) {
// 		location.reload();
// 	} else {
// 		alert('Произошла ошибка при удалении элемента.');
// 	}
// });
// });
// });