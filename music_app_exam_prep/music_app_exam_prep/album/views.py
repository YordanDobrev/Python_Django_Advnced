from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from music_app_exam_prep.album.forms import CreateAlbumForm, DeleteAlbumForm
from music_app_exam_prep.album.models import Album
from music_app_exam_prep.utils import get_user_obj


# Create your views here.

class AlbumCreateView(CreateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'album/album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'album/album-details.html'
    pk_url_kwarg = 'id'


class AlbumEditView(UpdateView):
    model = Album
    form_class = CreateAlbumForm
    template_name = 'album/album-edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


# def album_delete(request):
#     return render(request, 'album/album-delete.html')


class AlbumDeleteView(DeleteView):
    model = Album
    form_class = DeleteAlbumForm
    template_name = 'album/album-delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
