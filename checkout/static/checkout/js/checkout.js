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

        // Calculate the new grand total
        var deliveryCost = parseFloat($('#delivery-cost').val());
        var newGrandTotal = orderTotal + deliveryCost;

        // Update the grand total element
        $('#grand-total').text(newGrandTotal.toFixed(2) + " GBP");
    }

    // Listen for changes in the delivery type radio buttons
    $('input[name="delivery_type"]').on('change', function () {
        var selectedDeliveryType = $(this);
        updateHiddenDeliveryCost(selectedDeliveryType);
    });

    // Trigger the initial update when the page loads
    updateHiddenDeliveryCost(selectedDeliveryType);

    // Update the hidden-delivery-cost element's text based on the hidden input value
    var hiddenValue = parseFloat($('#delivery-cost').val()).toFixed(2);
    $('#hidden-delivery-cost').text(hiddenValue + " GBP");
});
