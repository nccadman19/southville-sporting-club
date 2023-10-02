from django.urls import path
from . import views
from .webhooks import my_webhook_view

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create-checkout-session/', views.CreateStripeCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('checkout-success/', views.checkout_success, name='checkout_success'),
    path('checkout-cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('my-webhook-view/', my_webhook_view, name='my_webhook_view'),
]