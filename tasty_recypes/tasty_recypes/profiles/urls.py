from django.urls import path
from tasty_recypes.profiles import views

urlpatterns = [
    path('details/', views.ProfileDetailsView.as_view(), name='profile_details'),
    path('create/', views.ProfileCreateView.as_view(), name='profile_create'),
    path('edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile_delete'),
]
