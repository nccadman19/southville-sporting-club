document.addEventListener('DOMContentLoaded', function () {
  var sidenavElems = document.querySelectorAll('.sidenav');
  var sidenavInstances = M.Sidenav.init(sidenavElems);
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
    closeIcon.style.display = "inline";
  });

  // When the search input loses focus (is clicked outside of)
  searchInput.addEventListener("blur", function () {
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

  // Function to show the cart overlay
  function showCartOverlay() {
    var cartOverlay = document.getElementById('cart-overlay');
    var closeOverlay = document.getElementById('close-cart-overlay');
    cartOverlay.style.display = 'flex';
    closeOverlay.style.display = 'block';
  }

  // Function to hide the cart overlay
  function hideCartOverlay() {
    var cartOverlay = document.getElementById('cart-overlay');
    cartOverlay.style.display = 'none';
  }

  // Add a click event listener to the bag icon
  document.getElementById('bag-icon').addEventListener('click', function (event) {
    showCartOverlay();
  });

  // Add a click event listener to the close button
  document.getElementById('close-cart-btn').addEventListener('click', function (event) {
    hideCartOverlay();
  });

  // Add a click event listener to the close overlay
  document.getElementById('close-cart-overlay').addEventListener('click', function (event) {
    hideCartOverlay();
    this.style.display = 'none';
  });

});
