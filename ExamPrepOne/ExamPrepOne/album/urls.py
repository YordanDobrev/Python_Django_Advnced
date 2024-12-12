from django.urls import path, include

from ExamPrepOne.album import views

urlpatterns = [
    path('add/', views.add_album, name='add_album'),
    path('<int:pk>/', include([
        path('details/', views.album_details, name='album_details'),
        path('edit/', views.album_edit, name='album_edit'),
        path('delete/', views.album_delete, name='album_delete'),
    ])),
]