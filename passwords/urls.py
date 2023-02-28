from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

urlpatterns = [
    # passwords/dashboard/
    path('dashboard/', login_required(views.Dashboard.as_view()), name='password_dashboard'),
]
