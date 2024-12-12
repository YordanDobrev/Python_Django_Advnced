from django.urls import path, include
from music_app_exam_prep.album import views

urlpatterns = [
    path('add/', views.AlbumCreateView.as_view(), name='add_album'),
    path('<int:id>/', include([
        path('details/', views.AlbumDetailsView.as_view(), name='album_details'),
        path('edit/', views.AlbumEditView.as_view(), name='album_edit'),
        path('delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
    ])),
]