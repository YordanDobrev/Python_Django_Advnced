from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from Artonia_v2.accounts import views
from Artonia_v2.accounts.views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', views.UserDetailsView.as_view(), name='user_details'),
        path('edit/', views.UserUpdateView.as_view(), name='user_edit'),
        path('delete/', views.UserDeleteView.as_view(), name='user_delete'),
    ])),
]
