from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from Artonia_v2.accounts.forms import CustomUserCreationForm, UserUpdateForm

UserModel = get_user_model()


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


class UserDetailsView(DetailView):
    model = UserModel
    template_name = 'registration/details-account.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(UpdateView):
    model = UserModel
    form_class = UserUpdateForm
    template_name = 'registration/edit-account.html'
    success_url = reverse_lazy('user_details')
    pk_field = 'pk'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('user_details', kwargs={'pk': self.object.pk})


class UserDeleteView(DeleteView):
    model = UserModel
    template_name = 'registration/delete-account.html'
    success_url = reverse_lazy('home')
    pk_field = 'pk'
