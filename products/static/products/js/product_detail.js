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

    let isFavorited = false; // Declare the isFavorited variable here

    function toggleHeartIcon() {
        isFavorited = !isFavorited;

        // Toggle the visibility of heart icons
        var filledHeartIcon = document.querySelector('.love-icon-filled');
        var outlineHeartIcon = document.querySelector('.love-icon-outline');

        if (isFavorited) {
            filledHeartIcon.style.display = 'block';
            outlineHeartIcon.style.display = 'none';
        } else {
            filledHeartIcon.style.display = 'none';
            outlineHeartIcon.style.display = 'block';
        }
    }

    // Add an event listener to toggle the heart icon when clicked
    var heartIcons = document.querySelectorAll('.material-icons.love-icon-filled, .material-icons.love-icon-outline');
    heartIcons.forEach(function (icon) {
        icon.addEventListener('click', toggleHeartIcon);
    });
});
