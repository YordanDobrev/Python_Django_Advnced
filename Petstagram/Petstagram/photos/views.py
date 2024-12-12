from django.shortcuts import render, redirect
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstagram.photos.models import Photo


# Create your views here.


def photo_add_page(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("home-page")

    context = {'form': form}

    return render(request, 'photos/photo-add-page.html', context)


def photo_edit_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('photo_edit', pk=pk)

    context = {
        'form': form,
        'photo': photo
    }

    return render(request, 'photos/photo-edit-page.html', context)


def photo_details_page(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()

    # comment_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        # 'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')
