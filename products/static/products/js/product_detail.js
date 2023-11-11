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

    // If there is more than one size, select the first one by default
    if (sizeButtons.length > 1) {
        var defaultSizeButton = Array.from(sizeButtons).find(button => !button.classList.contains('disabled'));

        if (defaultSizeButton) {
            defaultSizeButton.classList.add('selected');
            selectedSizeInput.value = defaultSizeButton.dataset.size;
        }
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

    // When the product details cards are clicked, change the icon and toggle between + and -
    var collapsibleHeaders = document.querySelectorAll('.collapsible-header.card-details');

    collapsibleHeaders.forEach(function (header) {
        header.addEventListener('click', function () {
            var icon = header.querySelector('.icon');
            var rotation = parseFloat(icon.style.transform.replace('rotate(', '').replace('deg)', ''));

            if (icon.innerHTML === '+') {
                icon.innerHTML = '-';
                icon.style.transform = 'rotate(0deg)';
            } else {
                icon.innerHTML = '+';
                icon.style.transform = 'rotate(90deg)';
            }
        });
    });

    // Image that can be enlarged on click
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems);

});
