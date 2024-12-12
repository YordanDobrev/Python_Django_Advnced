from django.urls import path

from RegularExam.author import views

urlpatterns = [
    path('create/', views.AuthorCreationView.as_view(), name='author_create'),
    path('edit/', views.AuthorUpdateView.as_view(), name='author_edit'),
    path('delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    path('details/', views.AuthorDetailsView.as_view(), name='author_details'),
]
