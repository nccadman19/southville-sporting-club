require('dotenv').config();

const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

(async () => {
    try {
        // Replace 'pi_XXXXXXXXX' with the actual PaymentIntent ID you want to check
        const paymentIntent = await stripe.paymentIntents.retrieve('pi_3O7nhkKWzixhQyQG1toTUkSY');

        if (paymentIntent.status === 'succeeded') {
            console.log('PaymentIntent succeeded!');
        } else {
            console.log('PaymentIntent did not succeed. Status: ' + paymentIntent.status);
        }
    } catch (error) {
        console.error('Error:', error.message);
    }
})();
