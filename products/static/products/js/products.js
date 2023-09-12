document.addEventListener('DOMContentLoaded', function () {
    // Initialise dropdown trigger for size dropdown menu
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

    // Get all the size buttons
    var sizeButtons = document.querySelectorAll('.product-form a.btn');

    // Attach a click event listener to each size button
    sizeButtons.forEach(function (button) {
        button.addEventListener('click', function (e) {
            e.preventDefault();

            // Deselect all buttons
            sizeButtons.forEach(function (btn) {
                btn.classList.remove('selected');
            });

            // Select the clicked button
            button.classList.add('selected');

            // Store the selected size in a variable or hidden input field here
            // For example, you can use the dataset property to store the size value
            var selectedSize = button.dataset.size;
        })
    })
});