from django.urls import path

from ExamPrep_WOS.profiles import views

urlpatterns = [
    path('create/', views.profile_creation, name='profile_create'),
    path('details/', views.profile_details, name='profile_details'),
    path('edit/', views.EditProfileView.as_view(), name='profile_edit'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
]