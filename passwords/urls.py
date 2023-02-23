from django.urls import path, include

from . import views

urlpatterns = [
    # passwords/dashboard/
    path('dashboard/', views.Dashboard.as_view(), name='password_dashboard'),
]
