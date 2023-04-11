from django.urls import path, include

from . import views

urlpatterns = [
    # users/register/
    path('register/', views.Register.as_view(), name="register"),
    # users/login/
    path('login/', views.Login.as_view(), name="login"),
    # users/logout/
    path('logout/', views.Logout.as_view(), name="logout"),
    # Adds a bunch of URLs (users/login, etc.)
    path('', include('django.contrib.auth.urls')),
]