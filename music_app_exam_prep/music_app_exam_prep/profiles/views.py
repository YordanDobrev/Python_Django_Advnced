from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from music_app_exam_prep.utils import get_user_obj


# Create your views here.

class ProfileDetailsView(DetailView):
    template_name = 'profile/profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()
