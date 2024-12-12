from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from tasty_recypes.profiles.forms import ProfileCreationForm, ProfileUpdateForm
from tasty_recypes.profiles.models import Profile
from tasty_recypes.utils import get_user_obj


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDetailsView(DetailView):
    template_name = 'profile/details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()
