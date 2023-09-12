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

            // Store the selected size in a variable or hidden input field here
            // For example, you can use the dataset property to store the size value
            var selectedSize = button.dataset.size;
        });
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
