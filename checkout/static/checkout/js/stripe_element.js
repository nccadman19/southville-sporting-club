var stripe = Stripe('pk_test_51NsY8IJwHrW3TDNzQ2w8broBMkBz0RKrsIF9bAa1Io2RoAouySFCICtyLXIRXbOmHHwWKYDAObMWv94L6T74gxBu00BJcw3j5X');
var elements = stripe.elements();

// Create an instance of the card Element
var card = elements.create('card');

// Add an instance of the card Element
card.mount('#card-element');

// Handle form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    // Use Stripe.js to create a token and handle the payment
    stripe.createToken(card, {
        name: document.getElementById('id_full_name').value,
        email: document.getElementById('id_email').value,
        // phone: document.getElementById('id_phone_number').value,
        address_line1: document.getElementById('id_street_address1').value,
        address_line2: document.getElementById('id_street_address2').value,
        address_city: document.getElementById('id_town_or_city').value,
        address_zip: document.getElementById('id_postcode').value,
        address_country: document.getElementById('id_country').value,
    }).then(function (result) {
        if (result.error) {
            // Show error to your customer
            console.error(result.error.message);
        } else {
            // Token created, you can now submit your form with the token ID
            // and handle the server-side processing.
            var token = result.token;
            // Send the token to your server for processing.
            // Handle the server-side logic to complete the payment.
        }
    });
});