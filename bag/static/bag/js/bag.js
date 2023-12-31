document.addEventListener('DOMContentLoaded', function () {

    // Function to show the cart overlay
    function showCartOverlay() {
        var cartOverlay = document.getElementById('cart-overlay');
        var closeOverlay = document.getElementById('close-cart-overlay');
        cartOverlay.style.display = 'flex';
        closeOverlay.style.display = 'block';

        // Attach click event listeners to all elements with the "remove-item" class
        var removeButtons = document.querySelectorAll('.remove-item');
        removeButtons.forEach(function (button) {
            button.addEventListener('click', removeItem);
        });
    }

    // Function to hide the cart overlay
    function hideCartOverlay() {
        var cartOverlay = document.getElementById('cart-overlay');
        var closeOverlay = document.getElementById('close-cart-overlay');
        cartOverlay.style.display = 'none';
        closeOverlay.style.display = 'none';
    }

    // Add a click event listener to the bag icon
    document.getElementById('bag-icon').addEventListener('click', function (event) {
        showCartOverlay();
    });

    // Add a click event listener to the close button
    document.getElementById('close-cart-btn').addEventListener('click', function (event) {
        hideCartOverlay();
    });

    // Add a click event listener to the close overlay
    document.getElementById('close-cart-overlay').addEventListener('click', function (event) {
        hideCartOverlay();
        this.style.display = 'none';
    });

    // Function to update the cart display
    function updateCartDisplay(cartData) {
        // Clear the existing cart content
        var cartContent = document.querySelector('.cart-item');
        cartContent.innerHTML = '';

        // Iterate through cartData and render cart items
        for (var item_id in cartData) {
            // Check if the property belongs to the object itself
            if (cartData.hasOwnProperty(item_id)) {
                // Create and append cart item elements to cartContent
                var cartItemElement = createCartItemElement(item_id, cartData[item_id]);
                cartContent.appendChild(cartItemElement);
            }
        }
    }

    // Function to create a cart item element
    function createCartItemElement(item_id, quantity) {
        var cartItemElement = document.createElement('div');
        cartItemElement.classList.add('cart-item');

        return cartItemElement;
    }

    // Modify the removeItem function to update the cart display
    function removeItem(event) {
        event.preventDefault();
        var removeButton = event.target;
        var item_id = removeButton.id.replace('remove_', '');
        var selected_size = removeButton.getAttribute('data-product_size');

        // Create a new XMLHttpRequest (AJAX request)
        var xhr = new XMLHttpRequest();
        xhr.open('POST', `/bag/remove/${item_id}/`, true);

        // Set the request header for CSRF protection
        xhr.setRequestHeader('X-CSRFToken', document.querySelector('meta[name="csrf-token"]').content);

        // Set the callback function when the request is complete
        xhr.onload = function () {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.status === 'success') {
                    console.log('AJAX request successful.'); // Log success

                    // Update the cart display after removing the item
                    updateCartDisplay(response.cart_data);
                    location.reload();
                } else {
                    console.error('AJAX request error:', response.message); // Log error
                }
            } else {
                console.error('AJAX request error:', xhr.statusText); // Log error
            }
        };

        // Set the POST data
        var formData = new FormData();
        formData.append('item_id', item_id);
        formData.append('selected_size', selected_size);
        xhr.send(formData);
    }
});
