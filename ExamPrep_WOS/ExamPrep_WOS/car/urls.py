from django.urls import path, include
from ExamPrep_WOS.car import views

urlpatterns = [
    path('catalogue/', views.car_catalog, name='catalog'),
    path('create/', views.CarCreateView.as_view(), name='car_create'),
    path('<int:id>/', include([
        path('details/', views.CarDetailsView.as_view(), name='car_details'),
        path('edit/', views.CarUpdateView.as_view(), name='car_edit'),
        path('delete/', views.CarDeleteView.as_view(), name='car_delete'),
    ])),
]