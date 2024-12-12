from django.urls import path

from Artonia_v2.artwork import views

urlpatterns = [
    path('', views.PublicArtworkListView.as_view(), name='public_artwork_list'),
]
