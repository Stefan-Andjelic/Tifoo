from django.urls import path, include

from . import views


urlpatterns = [
    # Django auth
    path('', include('django.contrib.auth.urls')),

    # User register and edit pages
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    # Dashboard page
    path('', views.dashboard, name='dashboard'),

    # User list and detail pages
    path('users/', views.user_list, name='user_list'),
    path('users/<username>/', views.user_detail, name='user_detail'),
]
