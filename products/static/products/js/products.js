document.addEventListener('DOMContentLoaded', function () {
    // Initialise dropdown trigger for size dropdown menu
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

    // Initialise the specific dropdown trigger with click option and coverTrigger
    var sortDropdownElem = document.querySelector('.sort-dropdown-trigger');
    var dropdownOptions = { alignment: 'right', coverTrigger: false, closeOnClick: true };
    var specificDropdownInstance = M.Dropdown.init(sortDropdownElem, dropdownOptions);

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

            // Log the selected size to the console (optional)
            console.log("Selected Size:", selectedSize);
        });
    });

    // Get the "Add to Bag" form
    var addToBagForm = document.querySelector('.form');

    // Attach a submit event listener to the "Add to Bag" form
    addToBagForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Find the selected size button within the product detail section
        var selectedSizeButton = document.querySelector('.product-size-button.selected');

        // If a size is selected, set it in the hidden input field
        if (selectedSizeButton) {
            var selectedSize = selectedSizeButton.dataset.size;
            document.getElementById("selected-size").value = selectedSize;
        }

        // Submit the form
        this.submit();
    });

    // Initialise the return to top button
    var backToTopBtn = document.getElementById('back-to-top');
    var backToTopContainer = document.getElementById('back-to-top-container');

    function toggleBackToTopButton() {
        if (window.scrollY > 300) { // Adjust the value as needed
            backToTopContainer.style.display = 'block';
        } else {
            backToTopContainer.style.display = 'none';
        }
    }

    // Attach a scroll event listener to the window
    window.addEventListener('scroll', toggleBackToTopButton);

    // Scroll to the top when the button is clicked
    backToTopBtn.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // For smooth scrolling behavior
        });
        backToTopBtn.classList.remove('waves-ripple');
    });
});
