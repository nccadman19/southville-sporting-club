from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('nothing-found/', views.nothing_found, name='nothing_found'),
]
