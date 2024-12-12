from django.urls import path, include
from django.views.generic import RedirectView

from ForumApp.posts.views import dashboard, details_page, PostCreateView, PostEditView, \
    PostDeleteView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', dashboard, name='dash'),
    path('add-post/', PostCreateView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', PostDeleteView.as_view(), name='delete-post'),
        path('details-post/', details_page, name='details-post'),
        path('edit-post/', PostEditView.as_view(), name='edit-post'),
    ])), path('redirect-home/', RedirectView.as_view(), name='redirect-home')
]
