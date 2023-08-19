(function ($) {
  $(function () {

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function () {
  // Initialize dropdown triggers with hover option and belowOrigin
  $(".dropdown-trigger").dropdown({ hover: true, coverTrigger: false });
});
