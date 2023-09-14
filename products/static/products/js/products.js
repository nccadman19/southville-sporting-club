document.addEventListener('DOMContentLoaded', function () {
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
