from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about, name="about-me"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
]
