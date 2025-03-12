document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.btn-addToCart');
	const categorieElements = document.querySelectorAll('.categorie');
    let productId

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
			productId = this.getAttribute('data-id');

            const send_id_url = "\\home\\send_id";
            const data = {
                "id": productId,
            }

            fetch(send_id_url, {
                "method": "POST",
                "headers": { "Content-Type": "application/json" },
                "body": JSON.stringify(data),
            })
			.then(response => {
				if (!response.ok) {
					throw new Error('Network response was not ok');
				}
				return response.json();
			})
			.then(data => {
				const qt = parseInt(data.quantity, 10);
				if (!isNaN(qt)) {
					const qtInCart = document.querySelector(`.qtInCart[data-id="${productId}"]`);
					qtInCart.innerText = (qt > 0) ? `${qt} items` : `Sold Out`;
				}
			})

        });
    });

});
