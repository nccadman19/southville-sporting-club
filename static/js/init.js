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