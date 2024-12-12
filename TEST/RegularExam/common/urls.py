from django.urls import path

from RegularExam.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]