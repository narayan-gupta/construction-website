from . import views

from django.urls import path

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('services', views.services, name='services'),
    path('careers', views.careers, name='careers'),
    path('planroom', views.planroom, name='planroom'),
    path('contact-us', views.contact, name='contact'),
]
