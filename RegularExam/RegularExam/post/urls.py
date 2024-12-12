from django.urls import path, include

from RegularExam.post import views

urlpatterns = [
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('<int:id>/', include([  # TO ASK IN SLIDO IF THIS IS A SLUG OR THE ID OF THE POST
        path('details/', views.PostDetailsView.as_view(), name='details_post'),
        path('edit/', views.PostEditView.as_view(), name='edit_post'),
        path('delete/', views.PostDeleteView.as_view(), name='delete_post'),
    ])),
]
