from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create-checkout-session/', views.CreateStripeCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('checkout-success/', views.checkout_success, name='checkout_success'),
    path('checkout-cancel/', views.checkout_cancel, name='checkout_cancel'),
]