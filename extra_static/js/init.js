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
  var searchInput = document.getElementById("search");
  var closeIcon = document.querySelector(".close-icon");
  var collapsibleHeaders = document.querySelectorAll('.collapsible-header');

  // When the search input gains focus (is clicked)
  searchInput.addEventListener("focus", function () {
    // Show the close icon
    closeIcon.style.display = "inline";
  });

  // When the search input loses focus (is clicked outside of)
  searchInput.addEventListener("blur", function () {
    // Hide the close icon
    closeIcon.style.display = "none";
  });

  // When the product details cards clicked shows respective icon
  collapsibleHeaders.forEach(function (header) {
    header.addEventListener('click', function () {
      var icon = header.querySelector('.icon');
      if (icon.innerHTML === '+') {
        icon.innerHTML = '-';
      } else {
        icon.innerHTML = '+';
      }
    });
  });

});
