document.addEventListener('DOMContentLoaded', function () {
    //const quantityInputs = document.querySelectorAll('.quantity-input');
    const increaseButtons = document.querySelectorAll('.increase');
    const decreaseButtons = document.querySelectorAll('.decrease');
    
    const totalPriceElement = document.getElementById('total-price');
    const removeButtons = document.querySelectorAll('.remove');

    function updateTotal() {
        let total = 0;
        document.querySelectorAll('.cart-item').forEach(item => {
            const price = parseFloat(item.dataset.price);
            const quantity = parseInt(item.querySelector('.quantity-display').textContent);
            total += price * quantity;
        });
        totalPriceElement.textContent = total.toFixed(2);
    }

     // Send product ID to Flask server
	function send_id(product_id) {
		const send_id_url = "\\cart\\send_id";
		let data = {
			"id": product_id,
		}
		fetch(send_id_url, {
			"method": "POST",
			"headers": { "Content-Type": "application/json" },
			"body": JSON.stringify(data),
		}).then()
	}

	// Send qt to Flask server
	function send_qt(product_id, qt, updateQt = () => {}, setSoldOut= () => {}) {
		const send_qt_url = "\\cart\\send_qt";
		let data = {
			"id": product_id,
			"qt": qt,
		}
		fetch(send_qt_url, {
			"method": "POST",
			"headers": { "Content-Type": "application/json" },
			"body": JSON.stringify(data),
		})
		.then(response => response.json())
		.then(data => {
			if('status' in data && data.status === "unavailable") {
				setSoldOut(product_id)
			}
			else {
				updateQt()
			}
		})
	}


    removeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const cartItem = this.closest('.cart-item');
            cartItem.remove();
            updateTotal();

			// Send product ID to Flask server
			send_id(this.getAttribute('data-id'))
        });
    });

    // button +
    increaseButtons.forEach(button => {
        button.addEventListener('click', function () {
            const quantityDisplay = this.previousElementSibling;
            let currentQuantity = parseInt(quantityDisplay.textContent);

            // Send qt to Flask server
            send_qt(
				this.getAttribute('data-id'), 
				currentQuantity + 1,
				() => {
					quantityDisplay.textContent = currentQuantity + 1;
					updateTotal()
				},
				(id) => {
					const soldOut = document.querySelector(`#soldOut[data-id="${id}"]`);
					soldOut.textContent = "Sold Out"
				}
			);
        });
    });

    // button -
    decreaseButtons.forEach(button => {
        button.addEventListener('click', function () {
            const quantityDisplay = this.nextElementSibling;
            let currentQuantity = parseInt(quantityDisplay.textContent);

            if (currentQuantity > 1) {
				// Send qt to Flask server
				send_qt(
					this.getAttribute('data-id'), 
					currentQuantity - 1,
					() => {
						quantityDisplay.textContent = currentQuantity - 1;
						updateTotal()
					},
					() => {}
				);
            }
        });
    });

    updateTotal();

});
