// Create an instance of the Stripe object with your publishable API key
var stripe = Stripe('STRIPE_PUBLIC_KEY');

// Attach the form submission handler to your form
document.getElementById('payment-form').addEventListener('submit', handleFormSubmit);

// Function to handle the form submission and initiate Stripe Checkout
function handleFormSubmit(event) {
    event.preventDefault();

    // Fetch the session_id from the server
    fetch('/create-checkout-session/', {
        method: 'POST',
        body: JSON.stringify({}),  // You can send additional data if needed
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        }
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log('Session ID:', data.session_id); // Log the session ID
            // Set the session_id value in the hidden input field
            document.getElementById('session_id').value = data.session_id;

            // Submit the form
            document.getElementById('payment-form').submit();
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
}