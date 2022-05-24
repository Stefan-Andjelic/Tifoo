from django.urls import path, include

from . import views


urlpatterns = [
    # Django auth
    path('', include('django.contrib.auth.urls')),

    # User register
    path('register/', views.register, name='register'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),
]
