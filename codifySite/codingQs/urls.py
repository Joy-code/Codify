from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('login.html', views.login, name='login'),
    path('stats.html', views.stats, name='stats'),
    path('reminders.html', views.reminders, name='reminders')
]