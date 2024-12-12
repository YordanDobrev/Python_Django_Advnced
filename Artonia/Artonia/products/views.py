from django.shortcuts import render, redirect, get_object_or_404

from Artonia.products.forms import ArtForm, MacrameForm
from Artonia.products.models import ArtPainting, Macrame


# Create your views here.

def index(request):
    art_paintings = request.GET.get('art_paintings', '')
    art_paintings = ArtPainting.objects.filter(name__icontains=art_paintings).order_by('-id')[:5]

    macrame = request.GET.get('macrame', '')
    macrame = Macrame.objects.filter(name__icontains=macrame).order_by('-id')[:5]

    context = {
        'art_paintings': art_paintings,
        'macrame': macrame,
    }

    return render(request, 'products_in_table.html', context)


def add_macrame(request):
    macrame_form = MacrameForm(request.POST or None, request.FILES)

    if request.method == 'POST':
        if macrame_form.is_valid():
            macrame_form.save()
            return redirect('dash')

    context = {
        'macrame_form': macrame_form,
    }

    return render(request, 'add-macrame.html', context)


def add_art_painting(request):
    art_form = ArtForm(request.POST or None, request.FILES)

    if request.method == 'POST':
        if art_form.is_valid():
            art_form.save()
            return redirect('dash')

    context = {
        'art_form': art_form,
    }

    return render(request, 'add-art-painting.html', context)


def edit_macrame(request, id):
    macrame = get_object_or_404(Macrame, id=id)  # Fetch the macrame object

    if request.method == 'POST':
        form = MacrameForm(request.POST, request.FILES, instance=macrame)
        if form.is_valid():
            form.save()
            return redirect('dash')  # Redirect after saving
    else:
        form = MacrameForm(instance=macrame)  # Load the form with macrame instance data

    context = {
        'form': form,
        'macrame': macrame,
    }

    return render(request, 'edit_macrame.html', context)


def edit_art_painting(request, id):
    art_painting = get_object_or_404(ArtPainting, id=id)  # Fetch the art_object object

    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES, instance=art_painting)
        if form.is_valid():
            form.save()
            return redirect('dash')  # Redirect after saving
    else:
        form = ArtForm(instance=art_painting)  # Load the form with art_painting instance data

    context = {
        'form': form,
        'art_painting': art_painting,
    }

    return render(request, 'edit_art_painting.html', context)
