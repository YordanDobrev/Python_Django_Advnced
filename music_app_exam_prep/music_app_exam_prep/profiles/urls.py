from django.urls import path
from music_app_exam_prep.profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailsView.as_view(), name='profile_details'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
]
