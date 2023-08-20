document.addEventListener('DOMContentLoaded', function () {
  // Initialize sidenav
  var sidenavElems = document.querySelectorAll('.sidenav');
  var sidenavInstances = M.Sidenav.init(sidenavElems);
  // Initialize dropdown triggers with hover option and belowOrigin
  var dropdownElems = document.querySelectorAll('.dropdown-trigger');
  var dropdownOptions = { hover: true, coverTrigger: false };
  var dropdownInstances = M.Dropdown.init(dropdownElems, dropdownOptions);
  var elems = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(elems, { accordion: false });
});
