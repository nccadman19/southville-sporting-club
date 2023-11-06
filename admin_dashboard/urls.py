from django.urls import path
from . import views

urlpatterns = [
    path('order-list/', views.order_list, name='order-list'),
    path('stock-list/', views.stock_list, name='stock-list'),
]
