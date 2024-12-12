from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from RegularExam.author.forms import AuthorCreateForm, AuthorUpdateForm
from RegularExam.author.models import Author
from RegularExam.utils import get_user_obj


class AuthorCreationView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create-author.html'
    success_url = reverse_lazy('home')


class AuthorDetailsView(DetailView):
    model = Author
    template_name = 'author/details-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorUpdateForm
    template_name = 'author/edit-author.html'
    success_url = reverse_lazy('author_details')

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/delete-author.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()
