from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('nothing-found/', views.nothing_found, name='nothing_found'),
]
