document.addEventListener('DOMContentLoaded', function () {
    // Initialize sidenav
    var sidenavElems = document.querySelectorAll('.sidenav');
    var sidenavInstances = M.Sidenav.init(sidenavElems);

    // Initialize the specific dropdown trigger with click option and coverTrigger
    var sortDropdownElem = document.querySelector('.sort-dropdown-trigger');
    var dropdownOptions = { alignment: 'right', coverTrigger: false, closeOnClick: true };
    var specificDropdownInstance = M.Dropdown.init(sortDropdownElem, dropdownOptions);

    // Initialize the return to top button
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
