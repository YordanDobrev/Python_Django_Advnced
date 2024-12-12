from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from Artonia_v2.art_painting.forms import CreateArtPaintingForm, EditArtPaintingForm, ArtPaintingDeleteForm, \
    EditArtBidForm
from Artonia_v2.art_painting.models import ArtPainting
from Artonia_v2.common.models import Product, Like


# Create your views here.
class CreateArtPaintingView(CreateView):
    model = Product
    form_class = CreateArtPaintingForm
    template_name = 'art_painting/create-art-painting.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateArtPaintingView(UpdateView):
    model = ArtPainting
    form_class = EditArtPaintingForm
    template_name = 'art_painting/edit-art-painting.html'
    success_url = reverse_lazy('dashboard')
    pk_field = 'pk'


class ArtPaintingDetailsView(DetailView):
    model = ArtPainting
    template_name = 'art_painting/details-art-painting.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        art = self.get_object()
        context['is_creator'] = self.request.user.pk == art.user_id
        context['closed_bid_date'] = date.today()
        context['likes'] = art.total_likes()

        if self.request.user.is_authenticated:
            content_type = ContentType.objects.get_for_model(ArtPainting)
            context['user_has_liked'] = Like.objects.filter(
                user=self.request.user,
                content_type=content_type,
                object_id=art.pk
            ).exists()
        else:
            context['user_has_liked'] = False

        return context


class ArtPaintingDeleteView(DeleteView):
    model = ArtPainting
    form_class = ArtPaintingDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'art_painting/delete-art-painting.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class LikeToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        art_painting = get_object_or_404(ArtPainting, pk=pk)
        content_type = ContentType.objects.get_for_model(ArtPainting)

        existing_like = Like.objects.filter(
            user=request.user,
            content_type=content_type,
            object_id=art_painting.pk
        )

        if existing_like.exists():
            existing_like.delete()
        else:
            Like.objects.create(
                user=request.user,
                content_type=content_type,
                object_id=art_painting.pk
            )

        return redirect(reverse_lazy('details_art-painting', kwargs={'pk': pk}))


class UpdateArtPaintingBidView(UpdateView):
    model = ArtPainting
    form_class = EditArtBidForm
    template_name = 'art_painting/edit-art-painting-bid.html'
    success_url = reverse_lazy('public_artwork_list')
    pk_field = 'pk'

    def form_valid(self, form):
        form.instance.bidder = self.request.user.username
        return super().form_valid(form)
