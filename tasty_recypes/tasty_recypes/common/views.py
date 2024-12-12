from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from tasty_recypes.profiles.forms import ProfileCreationForm
from tasty_recypes.recipe.models import Recipe
from tasty_recypes.utils import get_user_obj


# Create your views here.

class HomePage(ListView, BaseFormView):
    model = Recipe
    form_class = ProfileCreationForm
    success_url = reverse_lazy('home')

    def get_template_names(self, **kwargs):
        profile = get_user_obj()

        if profile:
            return ['home-page.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
