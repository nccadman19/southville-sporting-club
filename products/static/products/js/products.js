document.addEventListener('DOMContentLoaded', function () {
    // Get the elements related to the scroll-to-top button if they exist
    var backToTopBtn = document.getElementById('back-to-top');
    var backToTopContainer = document.getElementById('back-to-top-container');

    // Initialise the specific dropdown trigger with click option and coverTrigger
    var sortDropdownElem = document.querySelector('.sort-dropdown-trigger');
    var dropdownOptions = { alignment: 'right', coverTrigger: false, closeOnClick: true };
    var specificDropdownInstance = M.Dropdown.init(sortDropdownElem, dropdownOptions);

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

    var modals = document.querySelectorAll('.modal');
    var instances = M.Modal.init(modals);

    // Create objects to store the selected sizes and their quantities
    var selectedSizes = {};
    var sizeQuantities = {};

    // Populate the selected sizes from the 'id_sizes' input
    var initialSelectedSizes = $('#id_sizes').val();
    if (initialSelectedSizes) {
        initialSelectedSizes.split(', ').forEach(function (size) {
            selectedSizes[size] = 0;
        });
        updateHiddenInput();
    }

    // Loop through size containers in the HTML and extract size and quantity
    $('.size-container').each(function () {
        var size = $(this).find('label').text();
        var quantity = parseInt($(this).find('input[type="number"]').val(), 10) || 0;

        if (quantity > 0) {
            sizeQuantities[size] = quantity;
        }
    });

    // Assign the sizeQuantities object to the selectedSizes
    selectedSizes = sizeQuantities;

    // Update the hidden input
    updateHiddenInput();

    // Listen for changes on size checkboxes
    $('input[type="checkbox"]').off('change').on('change', function () {
        // Get the size from the checkbox's value
        var size = this.value; // Use the checkbox's value to get the size

        if (this.checked) {
            // Create a container for the size input
            var sizeContainer = document.createElement('div');
            sizeContainer.className = 'size-container';

            // Create a label for the size
            var sizeLabel = document.createElement('label');
            sizeLabel.textContent = size;

            // Create an input field for quantity
            var input = document.createElement('input');
            input.type = 'number';
            input.name = 'size-quantity-' + size;
            input.placeholder = 'Enter quantity';
            input.max = 999;

            // Append the label and input field to the size container
            sizeContainer.appendChild(sizeLabel);
            sizeContainer.appendChild(input);

            // Append the size container to the quantity-container
            $('#quantity-container').append(sizeContainer);

            // Handle quantity input changes using event delegation
            $(input).on('input', function () {
                selectedSizes[size] = parseInt(input.value, 10) || 0;
                updateHiddenInput();
            });

            // Add the size to the selected sizes object
            selectedSizes[size] = 0; // Initialize quantity to 0
        } else {
            // Remove the size and its quantity input field from the selected sizes object
            delete selectedSizes[size];

            // Remove the size container
            $('.size-container:has(input[name="size-quantity-' + size + '"])').remove();
            updateHiddenInput();
        }

        // Update the hidden input for 'id_sizes' with selected sizes
        $('#id_sizes').val(Object.keys(selectedSizes).join(', '));
        updateHiddenInput();
    });

    // Function to update the hidden input with selected sizes and quantities
    function updateHiddenInput() {
        // Create an object with the selected sizes and their quantities
        var sizeQuantity = {};
        Object.keys(selectedSizes).forEach(function (size) {
            sizeQuantity[size] = selectedSizes[size];
        });

        // Convert the sizeQuantity object to a JSON string and set it as a hidden field value
        $('input[name="size_quantity"]').val(JSON.stringify(sizeQuantity));
    }

    // Handle category selection
    $('#id_category').on('change', function () {
        // Get the selected categories
        var selectedCategories = $('#id_category option:selected');

        // Remove the "selected" attribute from all options
        $('#id_category option').removeAttr('selected');

        // Add the "selected" attribute to the selected options
        selectedCategories.attr('selected', 'selected');
    });

    // Handle form submission
    $('form').on('submit', function (e) {
        e.preventDefault(); // Prevent the default form submission

        // Submit the form (if needed) or perform any additional actions
        this.submit();
    });
});