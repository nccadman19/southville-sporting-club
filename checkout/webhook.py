import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    secret = settings.STRIPE_WEBHOOK

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key, secret
        )
    except ValueError as e:
        return JsonResponse({'error': 'Invalid payload'}, status=400)

    # Handle the specific event type (e.g., checkout.session.completed)
    if event.type == 'checkout.session.completed':
        # Perform actions here, e.g., mark an order as paid
        # You can access event.data.object for event-specific data
        # Print the event data (for testing purposes)
        print('Webhook received for checkout.session.completed event:')
        print(event.data.object)


        return JsonResponse({'status': 'Webhook received'}, status=200)

    return JsonResponse({'status': 'Webhook received'}, status=200)