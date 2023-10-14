from django.urls import path
from . import views, webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create-checkout-session/', views.CreateStripeCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('checkout-success/<str:order_number>/', views.checkout_success, name='checkout_success'),
    path('checkout-cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('stripe/webhook/', webhook.stripe_webhook, name='stripe_webhook'),
]