document.addEventListener('DOMContentLoaded', function () {
    // Initially, update the hidden input value based on the default selection
    var selectedDeliveryType = $('input[name="delivery_type"]:checked');
    updateHiddenDeliveryCost(selectedDeliveryType);

    // Define the updateHiddenDeliveryCost function
    function updateHiddenDeliveryCost(selectedDeliveryType) {
        // Get the cost value from the selected delivery type label
        var costText = selectedDeliveryType.siblings('span').text();

        // Extract the cost value using regular expressions
        var match = costText.match(/\(£([\d.]+)\)/);
        if (match) {
            var deliveryCost = parseFloat(match[1]);
            $('#delivery-cost').val(deliveryCost.toFixed(2));

            // Update the displayed delivery cost
            $('#hidden-delivery-cost').text(deliveryCost.toFixed(2) + " GBP");

            // Call the function to update the grand total
            updateGrandTotal();
        }
    }

    // Function to update the grand total based on the selected delivery method
    function updateGrandTotal() {
        // Get the order total from HTML
        var orderTotal = parseFloat(document.getElementById('order-total').textContent);
        var deliveryCost = parseFloat($('#delivery-cost').val());

        // Calculate the new grand total
        var newGrandTotal = orderTotal + deliveryCost;

        // Update the grand total elements
        $('#grand-total').text(newGrandTotal.toFixed(2) + " GBP");
        $('#grand-total-input').val(newGrandTotal.toFixed(2));
    }

    // Trigger the initial update when the page loads
    updateHiddenDeliveryCost(selectedDeliveryType);

    var saveInfoCheckbox = document.getElementById('id-save-info');

    saveInfoCheckbox.addEventListener('change', function () {
        if (!saveInfoCheckbox.checked) {
            saveInfoCheckbox.removeAttribute('checked');
        }
    });

    // Listen for changes in the delivery type radio buttons
    $('input[name="delivery_type"]').on('change', function () {
        var selectedDeliveryType = $(this);
        updateHiddenDeliveryCost(selectedDeliveryType);
    });

    // Function to update the user's profile information via AJAX
    function updateProfileInfo() {
        // Collect the user's information from the form
        var formData = {
            // Extract other form fields as needed
            'default_phone_number': $('#id_default_phone_number').val(),
            'default_country': $('#id_default_country').val(),
            'default_postcode': $('#id_default_postcode').val(),
            'default_town_or_city': $('#id_default_town_or_city').val(),
            'default_street_address1': $('#id_default_street_address1').val(),
            'default_street_address2': $('#id_default_street_address2').val(),
            'default_county': $('#id_default_county').val(),
        };

        // Send the data to the server using AJAX
        $.ajax({
            type: 'POST',
            url: '/update_profile/',  // Replace with your actual URL for updating the profile
            data: formData,
            success: function (data) {
                console.log('Profile information updated successfully');
            },
            error: function (error) {
                console.error('Error updating profile information');
            }
        });
    }
});
