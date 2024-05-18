from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from .import views

urlpatterns = [
   path('',views.index,name='index'),
   path('about/',views.about,name='about'),
   path('services/',views.services,name='services'),
   path('contact/',views.contact,name='contact'),
]
