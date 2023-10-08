document.addEventListener('DOMContentLoaded', function () {
  // Trigger sidenav menu on mobile
  var sidenavElems = document.querySelectorAll('.sidenav');
  var sidenavInstances = M.Sidenav.init(sidenavElems);

  // Dropdown menu items
  var dropdownElems = document.querySelectorAll('.dropdown-trigger');
  var dropdownOptions = { hover: true, coverTrigger: false };
  var dropdownInstances = M.Dropdown.init(dropdownElems, dropdownOptions);

  // Accordian menu on mobile sidenav
  var elems = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(elems, { accordion: false });

  // Select search and home logos 
  var searchInput = document.getElementById("search");
  var closeIcon = document.querySelector(".close-icon");
  var homeLogo = document.getElementById("home-logo");
  var isSearchFocused = false;

  // Initial z-index for the home logo
  homeLogo.style.zIndex = "1000";

  // When the search input gains focus (is clicked)
  searchInput.addEventListener("focus", function () {
    // Show the close icon
    closeIcon.style.display = "inline";

    if (!isSearchFocused) {
      // Adjust z-index when search is focused
      homeLogo.style.zIndex = "0";
      isSearchFocused = true;
    }
  });

  // Attach a click event listener to the close icon
  closeIcon.addEventListener('click', function (e) {
    e.preventDefault();

    // Hide the close icon
    closeIcon.style.display = "none";

    if (isSearchFocused) {
      // Restore z-index when close icon is clicked
      homeLogo.style.zIndex = "1000";
      isSearchFocused = false;
    }

    // Restore the background color
    searchInput.style.backgroundColor = "";
  });

  // When the search input loses focus (is clicked outside of)
  searchInput.addEventListener("blur", function () {
    // Hide the close icon
    closeIcon.style.display = "none";

    if (isSearchFocused) {
      // Restore z-index when search loses focus
      homeLogo.style.zIndex = "1000";
      isSearchFocused = false;
    }

    // Restore the background color
    searchInput.style.backgroundColor = "";
  });

  var toastContainer = document.getElementById('toast-container');
  if (toastContainer) {
    // Show the toast message container
    setTimeout(function () {
      toastContainer.style.opacity = '1';
    }, 100); // Wait for a brief moment to start the animation

    // Slide out and remove the toast message container
    setTimeout(function () {
      toastContainer.style.transition = 'transform 0.5s ease, opacity 0.5s ease';
      toastContainer.style.transform = 'translateX(100%)';
      toastContainer.style.opacity = '0';

      // Remove the container after the animation finishes (0.5 seconds)
      setTimeout(function () {
        toastContainer.remove();
      }, 500);
    }, 4000);
  }
});