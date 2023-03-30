from django.urls import path, include

from . import views

urlpatterns = [
    # brochure/home/
    path('home/', views.Home.as_view(), name='home')
]
