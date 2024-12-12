from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from Artonia_v2.common.models import Product, Like
from Artonia_v2.macrame.forms import CreateMacrameForm, EditMacrameForm, MacrameDeleteForm, EditMacrameBidForm
from Artonia_v2.macrame.models import Macrame


class CreateMacrameView(CreateView):
    model = Product
    form_class = CreateMacrameForm
    template_name = 'macrame/create-macrame.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateMacrameView(UpdateView):
    model = Macrame
    form_class = EditMacrameForm
    template_name = 'macrame/edit-macrame.html'
    success_url = reverse_lazy('dashboard')
    pk_field = 'pk'


class MacrameDetailsView(DetailView):
    model = Macrame
    template_name = 'macrame/details-macrame.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        macrame = self.get_object()
        context['is_creator'] = self.request.user.pk == macrame.user_id
        context['closed_bid_date'] = date.today()
        context['likes'] = macrame.total_likes()

        # Check if the current user has liked this macramé
        if self.request.user.is_authenticated:
            content_type = ContentType.objects.get_for_model(Macrame)
            context['user_has_liked'] = Like.objects.filter(
                user=self.request.user,
                content_type=content_type,
                object_id=macrame.pk
            ).exists()
        else:
            context['user_has_liked'] = False

        return context


class MacrameDeleteView(DeleteView):
    model = Macrame
    form_class = MacrameDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'macrame/delete-macrame.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class UpdateMacrameBidView(UpdateView):
    model = Macrame
    form_class = EditMacrameBidForm
    template_name = 'macrame/edit-macrame-bid.html'
    success_url = reverse_lazy('public_artwork_list')
    pk_field = 'pk'

    def form_valid(self, form):
        form.instance.bidder = self.request.user.username
        return super().form_valid(form)


class LikeToggleView(LoginRequiredMixin, View):
    def post(self, request, pk):
        macrame = get_object_or_404(Macrame, pk=pk)

        content_type = ContentType.objects.get_for_model(Macrame)

        existing_like = Like.objects.filter(
            user=request.user,
            content_type=content_type,
            object_id=macrame.pk
        )

        if existing_like.exists():
            existing_like.delete()
        else:
            Like.objects.create(
                user=request.user,
                content_type=content_type,
                object_id=macrame.pk
            )

        return redirect(reverse_lazy('details_macrame', kwargs={'pk': pk}))
