from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shipping/', views.shipping, name='shipping'),
    path('terms/', views.terms, name='terms'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sustainability/', views.sustainability, name='sustainability'),
    path('error/', views.error, name='error'),
    path('500/', views.server_error, name='server-error'),
    re_path(r'^.*/$', views.error, name='catch-all-error'),
]
