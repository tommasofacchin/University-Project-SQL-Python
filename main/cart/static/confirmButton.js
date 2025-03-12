document.addEventListener('DOMContentLoaded', function () {
    const confirmButton = document.querySelector('.confirm-order');

    confirmButton.addEventListener('click', function(event) {
        event.preventDefault();
        document.getElementById('order-form').submit();
    });
});
