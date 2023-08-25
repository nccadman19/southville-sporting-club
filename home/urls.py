from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shipping/', views.shipping, name='shipping'),
    path('terms/', views.terms, name='terms'),
]
