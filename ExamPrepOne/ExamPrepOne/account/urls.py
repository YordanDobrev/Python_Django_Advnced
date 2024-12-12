from django.urls import path, include

from ExamPrepOne.account import views

urlpatterns = [
    path('', views.home, name='index'),
    path('profile/', include([
        path('details/', views.profile_details, name='profile-details'),
        path('delete/', views.DeleteProfileView.as_view(), name='profile-delete'),
    ])),
]