document.addEventListener('DOMContentLoaded', function () {
    // Get the elements related to the scroll-to-top button if they exist
    var backToTopBtn = document.getElementById('back-to-top');
    var backToTopContainer = document.getElementById('back-to-top-container');

    // Initialise the specific dropdown trigger with click option and coverTrigger
    var sortDropdownElem = document.querySelector('.sort-dropdown-trigger');
    var dropdownOptions = { alignment: 'right', coverTrigger: false, closeOnClick: true };
    var specificDropdownInstance = M.Dropdown.init(sortDropdownElem, dropdownOptions);

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

    // Add a delete item popup modal 
    var modals = document.querySelectorAll('.modal');
    var instances = M.Modal.init(modals);
});