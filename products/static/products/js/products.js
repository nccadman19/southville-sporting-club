// Define the validateForm function in the global
function validateForm() {
    var selectedSize = document.getElementById("selected-size").value;
    if (selectedSize === "") {
        alert("Please select a size.");
        return false;
    }
    return true;
}

document.addEventListener('DOMContentLoaded', function () {
    // Get all the size buttons within the product detail section
    var sizeButtons = document.querySelectorAll('.product-detail .product-size-button');

    // Initialise a variable to store the selected size
    var selectedSize = null;

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
});

document.addEventListener('DOMContentLoaded', function () {
    // ... Other code ...

    // Get the elements related to the scroll-to-top button if they exist
    var backToTopBtn = document.getElementById('back-to-top');
    var backToTopContainer = document.getElementById('back-to-top-container');

    // Attach the scroll-to-top button functionality if the elements exist
    if (backToTopBtn && backToTopContainer) {
        function toggleBackToTopButton() {
            if (window.scrollY > 300) {
                backToTopContainer.style.display = 'block';
            } else {
                backToTopContainer.style.display = 'none';
            }
        }

        window.addEventListener('scroll', toggleBackToTopButton);

        backToTopBtn.addEventListener('click', function () {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
            backToTopBtn.classList.remove('waves-ripple');
        });
    }
});
