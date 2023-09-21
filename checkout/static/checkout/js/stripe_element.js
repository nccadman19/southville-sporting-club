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
    stripe.createToken(card).then(function (result) {
        if (result.error) {
            // Show error to your customer
            console.error(result.error.message);
        } else {
            // Find out how to add the code to link databases
        }
    });
});