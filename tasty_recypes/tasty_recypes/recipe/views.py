from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from tasty_recypes.recipe.forms import RecipeCreateForm, RecipeDeleteForm
from tasty_recypes.recipe.models import Recipe
from tasty_recypes.utils import get_user_obj


# Create your views here.


def recipe_catalog(request):
    profile = get_user_obj()
    recipes = Recipe.objects.filter(pk=profile.pk)

    context = {
        'profile': profile,
        'recipes': recipes,
    }

    return render(request, 'recipe/catalogue.html', context)


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe/create-recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe/details-recipe.html'
    pk_url_kwarg = 'id'
    context_object_name = 'recipe'


class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeCreateForm
    template_name = 'recipe/edit-recipe.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


class RecipeDeleteView(DeleteView):
    model = Recipe
    form_class = RecipeDeleteForm
    template_name = 'recipe/delete-recipe.html'
    success_url = reverse_lazy('catalogue')
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
