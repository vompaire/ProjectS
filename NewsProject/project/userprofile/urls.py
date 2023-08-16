from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.view_profile, name='view_profile')
]