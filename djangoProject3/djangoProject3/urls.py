"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from FitUp.views import index, Reservations, Payments, Clients, Coaches, Trainings, ReservationCreate, RateCoach, PaymentCreate, login_user, ReservationEdit
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('Reservations/', Reservations, name="Reservations"),
    path('ReservationCreate/', ReservationCreate, name="ReservationCreate"),
    path('ReservationEdit/<int:pk>', ReservationEdit, name="ReservationEdit"),
    path('Trainings/', Trainings, name="Trainings"),
    path('Coaches/', Coaches, name="Coaches"),
    path('RateCoach/', RateCoach, name="RateCoach"),
    path('Clients/', Clients, name="Clients"),
    path('Payments/', Payments, name="Payments"),
    path('PaymentCrete/', PaymentCreate, name="PaymentCreate"),
    path('login/', login_user, name="Login_user"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='indexx'),

]
