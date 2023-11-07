from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('order-list/', views.order_list, name='order_list'),
    path('stock-list/', views.stock_list, name='stock_list'),
]
