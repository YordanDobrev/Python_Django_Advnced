from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from ExamPrepOne.account.forms import ProfileCreationForm, BaseProfile
from ExamPrepOne.account.models import Profile
from ExamPrepOne.album.models import Album


# Create your views here.

def home_view(request):
    # If the user is authenticated, check if they have a profile
    if request.user.is_authenticated:
        try:
            # Get profile by current logged in user
            profile = Profile.objects.get(username=request.user)

            # Get all albums belonging to the profile (assuming 'owner' is the profile in Album model)
            albums = Album.objects.get(owner_id=request.user.pk)

            context = {
                'profile': profile,
                'albums': albums,
            }

            # Render the home page with profile and album information
            return render(request, 'home-with-profile.html', context)

        except Profile.DoesNotExist:
            # If no profile exists for the user, render the form to create one
            form = ProfileCreationForm(request.POST or None, request.FILES or None)

            if form.is_valid():
                # Save the new profile
                profile = form.save(commit=False)
                profile.user = request.user  # Associate the profile with the current user
                profile.save()

                # Redirect to the home page with the new profile
                return redirect('index')

            context = {
                'form': form,
                'errors': form.errors,
            }
            return render(request, 'home-no-profile.html', context)
    else:
        # If the user is not authenticated, you can redirect them to the login page or handle it appropriately
        return redirect('home-no-profile.html')


def home(request):

    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, pk=request.user.id)

        albums = Album.objects.filter(owner=profile)

        context = {
            'profile': profile,
            'albums': albums,
        }

        # Profile exists, render the home page with profile information
        return render(request, 'home-with-profile.html', context)
    else:
        # If POST request, handle form submission for profile creation

        profile_form = ProfileCreationForm(request.POST or None)

        if request.method == 'POST':
            if profile_form.is_valid():
                profile_form.save()
                return redirect('index')

        context = {
            'profile_form': profile_form,
        }

        return render(request, 'home-no-profile.html', context)


def home_with_profile(request, pk: int):
    profile = get_object_or_404(Profile, pk=pk)
    albums = profile.albums.all()

    context = {
        'profile': profile,
        'albums': albums,
    }

    return render(request, 'home-with-profile.html', context)


def profile_details(request):
    profile = get_object_or_404(Profile, pk=request.user.id)

    context = {
        'profile': profile,
    }

    return render(request, 'profile-details.html', context)


class DeleteProfileView(View):
    model = Profile
    context_object_name = 'profile'
    success_url = 'profile-delete.html'

# def profile_delete(request):
#     return render(request, 'profile-delete.html', context=None)
