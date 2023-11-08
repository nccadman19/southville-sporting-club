document.addEventListener('DOMContentLoaded', function () {
  // Trigger sidenav menu on mobile
  var sidenavElems = document.querySelectorAll('.sidenav');
  var sidenavInstances = M.Sidenav.init(sidenavElems);

  // Dropdown menu items
  var dropdownElems = document.querySelectorAll('.dropdown-trigger:not(.profile-trigger)');
  var dropdownOptions = { hover: true, coverTrigger: false };
  var dropdownInstances = M.Dropdown.init(dropdownElems, dropdownOptions);

  // Dropdown profile icon
  var elems = document.querySelectorAll('.profile-trigger');
  var instances = M.Dropdown.init(elems);
  var instance = M.Dropdown.getInstance(elems);

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

  // Add click event listener to the profile icon
  var profileIcon = document.querySelector('.profile-trigger');
  if (profileIcon) {
    profileIcon.addEventListener('click', function (event) {
      // Initialize the profile dropdown with the constrainWidth option set to false
      var profileDropdownOptions = { constrainWidth: false };
      var profileDropdownInstance = M.Dropdown.init(profileIcon, profileDropdownOptions);

      // Open the profile dropdown
      if (profileDropdownInstance) {
        profileDropdownInstance.open();
      }
    });
  }

  // Get the elements related to the scroll-to-top button if they exist
  var backToTopBtn = document.getElementById('back-to-top');
  var backToTopContainer = document.getElementById('back-to-top-container');

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
});