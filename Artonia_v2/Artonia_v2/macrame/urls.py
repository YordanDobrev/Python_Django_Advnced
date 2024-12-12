from django.urls import path, include

from Artonia_v2.macrame import views

urlpatterns = [
    path('create/', views.CreateMacrameView.as_view(), name='create_macrame'),
    path('<int:pk>/', include([
        path('edit/', views.UpdateMacrameView.as_view(), name='edit_macrame'),
        path('details/', views.MacrameDetailsView.as_view(), name='details_macrame'),
        path('delete/', views.MacrameDeleteView.as_view(), name='delete_macrame'),
        path('bid/', views.UpdateMacrameBidView.as_view(), name='bid_macrame'),
        path('like/', views.LikeToggleView.as_view(), name='like_toggle'),
    ]))]
