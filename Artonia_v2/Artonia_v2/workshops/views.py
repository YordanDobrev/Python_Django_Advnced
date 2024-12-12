from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from Artonia_v2.workshops.forms import CreateWorkshopForm, DeleteWorkshopForm, UpdateWorkshopForm, \
    WorkshopRegistrationForm
from Artonia_v2.workshops.models import Workshop, WorkshopRegistration
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

UserModel = get_user_model()


# Create your views here.

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshops/workshop_list.html'
    context_object_name = 'workshops'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_instructor'] = self.request.user.groups.filter(name='Instructor').exists()
        return context


class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshops/workshop_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workshop = self.get_object()
        context['is_creator'] = self.request.user == workshop.instructor
        return context


class WorkshopCreateView(LoginRequiredMixin, CreateView):
    model = Workshop
    form_class = CreateWorkshopForm
    template_name = 'workshops/workshop_create.html'
    success_url = reverse_lazy('workshop-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.instructor = self.request.user
        return super().form_valid(form)


class WorkshopDeleteView(LoginRequiredMixin, DeleteView):
    model = Workshop
    form_class = DeleteWorkshopForm
    pk_url_kwarg = 'pk'
    template_name = 'workshops/workshop_delete.html'
    success_url = reverse_lazy('workshop-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workshop_list'] = Workshop.objects.all()
        return context

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class WorkshopUpdateView(LoginRequiredMixin, UpdateView):
    model = Workshop
    form_class = UpdateWorkshopForm
    template_name = 'workshops/workshop_edit.html'
    success_url = reverse_lazy('workshop-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workshop_list'] = Workshop.objects.all()

        return context

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


@login_required
def workshop_register(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)

    if request.method == 'POST':
        form = WorkshopRegistrationForm(
            request.POST,
            user=request.user,
            workshop=workshop
        )
        if form.is_valid():
            registration = form.save(commit=False)
            registration.participant = request.user
            registration.workshop = workshop
            registration.save()
            messages.success(request, 'Successfully registered for the workshop!')
            return redirect('workshop-list')
        else:
            messages.error(request, 'Registration failed. Please check the errors below.')

    else:
        form = WorkshopRegistrationForm(
            user=request.user,
            workshop=workshop
        )

    return render(request, 'workshops/workshop_register.html', {
        'workshop': workshop,
        'form': form,
    })


@login_required
def cancel_registration(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)

    if request.method == 'POST':
        registration = get_object_or_404(
            WorkshopRegistration,
            workshop=workshop,
            participant=request.user
        )
        registration.delete()
        messages.success(request, "Your workshop registration has been cancelled.")
        return redirect('workshop-list')

    return render(request, 'workshops/workshop_cancel_registration.html', {
        'workshop': workshop
    })
