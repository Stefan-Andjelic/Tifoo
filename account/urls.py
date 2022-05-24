from django.urls import path, include

from . import views


urlpatterns = [
    # Django auth
    path('', include('django.contrib.auth.urls')),

    # User register and edit pages
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),
]
