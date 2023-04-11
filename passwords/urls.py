from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views

urlpatterns = [
    # passwords/dashboard/
    path('dashboard/', login_required(views.Dashboard.as_view()), name='passwords_dashboard'),
    # passwords/#
    path('<int:pk>/', login_required(views.Detail.as_view()), name='passwords_detail'),
    # passwords/#/edit
    path('<int:pk>/edit/', login_required(views.Edit.as_view()), name='passwords_edit'),
    # passwords/create
    path('create/', login_required(views.Create.as_view()), name='passwords_create'),
    # passwords/delete
    path('<int:pk>/delete/', login_required(views.Delete.as_view()), name='passwords_delete'),
]
