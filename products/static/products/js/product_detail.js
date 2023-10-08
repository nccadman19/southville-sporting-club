document.addEventListener('DOMContentLoaded', function () {
    // Get all the size buttons within the product detail section
    var sizeButtons = document.querySelectorAll('.product-detail .product-size-button');

    // Initialise a variable to store the selected size
    var selectedSize = null;

    // Get the hidden input field for selected size
    var selectedSizeInput = document.getElementById("selected-size");

    // Set "One Size" as the default selected size if it's available as an option
    if (document.querySelector('.product-size-button[data-size="One Size"]')) {
        selectedSizeInput.value = "One Size";
    }

    // Attach a click event listener to each size button
    sizeButtons.forEach(function (button) {
        button.addEventListener('click', function (e) {
            e.preventDefault();

            // Deselect all buttons within the product detail section
            sizeButtons.forEach(function (btn) {
                btn.classList.remove('selected');
            });

            // Select the clicked button
            button.classList.add('selected');

            // Store the selected size in the variable
            selectedSize = button.dataset.size;

            // Update the hidden input field immediately
            document.getElementById("selected-size").value = selectedSize;
        });
    });

    // Get the "Add to Bag" form
    var addToBagForm = document.querySelector('.form');

    // Attach a submit event listener to the "Add to Bag" form
    addToBagForm.addEventListener('submit', function (e) {
        // Validate the selected size
        var selectedSize = document.getElementById("selected-size").value;
        if (selectedSize === "") {
            e.preventDefault(); // Prevent form submission
            alert("Please select a size.");
        }
    });

    // When the product details cards clicked shows respective icon
    var collapsibleHeaders = document.querySelectorAll('.collapsible-header-product');

    // Check if there are collapsible headers with icons on the page
    var collapsibleHeadersProduct = document.querySelectorAll('.collapsible-header-product');

    if (collapsibleHeadersProduct.length > 0) {
        // Attach click event listener to collapsible headers with icons
        collapsibleHeadersProduct.forEach(function (header) {
            header.addEventListener('click', function () {
                var icon = header.querySelector('.icon');
                if (icon.innerHTML === '+') {
                    icon.innerHTML = '-';
                } else {
                    icon.innerHTML = '+';
                }
            });
        });
    }
});