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

    // Function to adjust the cart's height based on its content
    function adjustCartHeight() {
        var cartOverlay = document.getElementById('cart-overlay');
        var cartItems = document.querySelectorAll('.cart-item');
        var totalHeight = 0;

        // Calculate the total height of all cart items
        cartItems.forEach(function (item) {
            totalHeight += item.scrollHeight;
        });

        // Set the cart's height to match the total height of cart items
        cartOverlay.style.height = totalHeight + 'px';
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
            // Create and append cart item elements to cartContent
            var cartItemElement = createCartItemElement(item_id, cartData[item_id]);
            cartContent.appendChild(cartItemElement);
        }

        // Update other cart-related information (subtotal, total, etc.) if needed
    }

    // Function to create a cart item element
    function createCartItemElement(item_id, quantity) {
        // Create and return a cart item element based on the item_id and quantity
        // You can generate the HTML structure for a cart item here
        // Example:
        var cartItemElement = document.createElement('div');
        cartItemElement.classList.add('cart-item');
        // Add other HTML and data attributes to the cart item element
        // ...

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
        xhr.setRequestHeader('X-CSRFToken', document.querySelector('input[name=csrfmiddlewaretoken]').value);

        // Set the callback function when the request is complete
        xhr.onload = function () {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.status === 'success') {
                    console.log('AJAX request successful.'); // Log success

                    // Update the cart display after removing the item
                    updateCartDisplay(response.cart_data);
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
        formData.append('selected_size', selected_size); // Add selected_size to the POST data
        xhr.send(formData);
    }
});
