from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from music_app_exam_prep.album.models import Album
from music_app_exam_prep.profiles.forms import ProfileCreationForm
from music_app_exam_prep.utils import get_user_obj


# Create your views here.

class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreationForm
    success_url = reverse_lazy('home')

    def get_template_names(self):
        profile = get_user_obj()
        if not profile:
            return ['common/home-no-profile.html']

        return ['common/home-with-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
