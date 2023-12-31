from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shipping/', views.shipping, name='shipping'),
    path('terms/', views.terms, name='terms'),
    path('about/', views.about, name='about'),
    path('sustainability/', views.sustainability, name='sustainability'),
]
