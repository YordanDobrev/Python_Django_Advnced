from django.urls import path

from tasty_recypes.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]
