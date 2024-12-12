from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from ExamPrep_WOS.profiles.forms import ProfileCreateForm, ProfileUpdateForm
from ExamPrep_WOS.profiles.models import Profile
from ExamPrep_WOS.utils import get_user_obj


# Create your views here.
#
# class ProfileCreateView(CreateView):
#     model = Profile
#     form_class = ProfileCreateForm
#     template_name = 'profile/profile-create.html'
#     success_url = reverse_lazy('catalog')


def profile_creation(request):
    form = ProfileCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    base_profile = get_user_obj()
    profile = Profile.objects.get(id=base_profile.id)

    if profile.first_name is None and profile.last_name is None:
        full_name = "No Full Name"
    elif profile.first_name is None and profile.last_name is not None:
        full_name = profile.last_name
    elif profile.first_name is not None and profile.last_name is None:
        full_name = profile.first_name
    else:
        full_name = profile.first_name + " " + profile.last_name

    price = profile.car_set.aggregate(total_price=Sum('price'))['total_price']

    context = {
        'profile': profile,
        'full_name': full_name,
        'price': price
    }

    return render(request, 'profile/profile-details.html', context)

class EditProfileView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile/profile-edit.html'
    success_url = reverse_lazy('profile_details')

    def get_object(self, queryset=None):
        return get_user_obj()


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')


class ProfileDeleteView(DeleteView):
    template_name = 'profile/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()
