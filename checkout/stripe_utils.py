import stripe
from django.conf import settings

def get_metadata_from_stripe(session_id):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        session = stripe.checkout.Session.retrieve(session_id, expand=['line_items'])
        metadata = session['metadata']
        return metadata
    except stripe.error.StripeError as e:
        # Handle any Stripe API errors here
        return None
