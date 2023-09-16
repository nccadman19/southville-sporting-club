// Define the validateForm function in the global scope
function validateForm() {
    var selectedSize = document.getElementById("selected-size").value;
    if (selectedSize === "" && !sizeButtons[0].classList.contains('selected') && sizeButtons.length > 1) {
        alert("Please select a size.");
        return false;
    }
    return true;
}

document.addEventListener('DOMContentLoaded', function () {
    // Get all the size buttons within the product detail section
    var sizeButtons = document.querySelectorAll('.product-detail .product-size-button');

    // Get the hidden input field for selected size
    var selectedSizeInput = document.getElementById("selected-size");

    // Attach a click event listener to each size button
    sizeButtons.forEach(function (button) {
        button.addEventListener('click', function (e) {
            e.preventDefault();

            // Check if the button is already selected
            if (button.classList.contains('selected')) {
                // Deselect the button
                button.classList.remove('selected');
                selectedSizeInput.value = ''; // Clear the selected size
            } else {
                // Deselect all buttons within the product detail section
                sizeButtons.forEach(function (btn) {
                    btn.classList.remove('selected');
                });

                // Select the clicked button
                button.classList.add('selected');

                // Store the selected size in the hidden input field
                selectedSizeInput.value = button.dataset.size;
            }
        });
    });

    // Get the "Add to Bag" form
    var addToBagForm = document.querySelector('.form');

    // Attach a submit event listener to the "Add to Bag" form
    addToBagForm.addEventListener('submit', function (e) {
        // Validate the form using the validateForm function
        var selectedSize = selectedSizeInput.value;
        if (selectedSize === "" && !sizeButtons[0].classList.contains('selected')) {
            e.preventDefault(); // Prevent form submission
            alert("Please select a size.");
        }
    });

    // When the product details cards are clicked, show respective icon
    var collapsibleHeaders = document.querySelectorAll('.collapsible-header-product');

    collapsibleHeaders.forEach(function (header) {
        header.addEventListener('click', function () {
            var icon = header.querySelector('.icon');
            if (icon.innerHTML === '+') {
                icon.innerHTML = '-';
            } else {
                icon.innerHTML = '+';
            }
        });
    });
});
