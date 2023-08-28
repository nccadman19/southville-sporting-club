document.addEventListener('DOMContentLoaded', function () {
    // Initialize sidenav
    var sidenavElems = document.querySelectorAll('.sidenav');
    var sidenavInstances = M.Sidenav.init(sidenavElems);

    // Initialize the specific dropdown trigger with click option and coverTrigger
    var specificDropdownElem = document.querySelector('.specific-dropdown-trigger');
    var dropdownOptions = { alignment: 'right', coverTrigger: false, closeOnClick: true };
    var specificDropdownInstance = M.Dropdown.init(specificDropdownElem, dropdownOptions);

    // ...rest of your JavaScript code
});
