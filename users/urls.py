from django.urls import path
from .views import register, profile, custom_login_view, search_users, public_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', custom_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('search/', search_users, name='search_users'),
    path('profile/<str:username>/', public_profile, name='public_profile'),
]
