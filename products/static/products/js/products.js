document.addEventListener('DOMContentLoaded', function () {
    // Initialise the specific dropdown trigger with click option and coverTrigger
    var sortDropdownElem = document.querySelector('.sort-dropdown-trigger');
    var dropdownOptions = { alignment: 'right', coverTrigger: false, closeOnClick: true };
    var specificDropdownInstance = M.Dropdown.init(sortDropdownElem, dropdownOptions);

    // Add a delete item popup modal 
    var modals = document.querySelectorAll('.modal');
    var instances = M.Modal.init(modals);
});