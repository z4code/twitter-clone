# urls.py
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('profiles/', views.profiles, name='profiles'),
	path('profile/<int:id>/', views.profile, name='profile'),
]