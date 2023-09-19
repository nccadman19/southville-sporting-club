document.addEventListener('DOMContentLoaded', function () {

    // Function to show the cart overlay
    function showCartOverlay() {
        var cartOverlay = document.getElementById('cart-overlay');
        var closeOverlay = document.getElementById('close-cart-overlay');
        cartOverlay.style.display = 'flex';
        closeOverlay.style.display = 'block';
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

    // Function to handle the click event on "Remove" buttons
    function removeItem(event) {
        event.preventDefault();
        var removeButton = event.target;
        var item_id = removeButton.id.replace('remove_', '');

        console.log('Item ID to remove:', item_id); // Log the item ID

        // Create a new XMLHttpRequest (AJAX request)
        var xhr = new XMLHttpRequest();
        xhr.open('POST', `/remove/${item_id}/`, true); // Use template literals to construct the URL

        // Set the request header for CSRF protection
        xhr.setRequestHeader('X-CSRFToken', document.querySelector('input[name=csrfmiddlewaretoken]').value);

        // Set the callback function when the request is complete
        xhr.onload = function () {
            if (xhr.status === 200) {
                console.log('AJAX request successful.'); // Log success
                // Update the cart overlay with the response data
                document.querySelector('#cart-overlay').innerHTML = xhr.responseText;
            } else {
                console.error('AJAX request error:', xhr.statusText); // Log error
            }
        };

        // Send the AJAX request with an empty body
        xhr.send();
    }


    // Attach click event listeners to all elements with the "remove-item" class
    var removeButtons = document.querySelectorAll('.remove-item');
    removeButtons.forEach(function (button) {
        button.addEventListener('click', removeItem);
    });
});
