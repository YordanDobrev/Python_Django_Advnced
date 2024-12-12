from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from ExamPrep_WOS.car.forms import CarCreateForm, CarDeleteForm
from ExamPrep_WOS.car.models import Car
from ExamPrep_WOS.utils import get_user_obj


def car_catalog(request):
    profile = get_user_obj()
    cars = profile.car_set.all()

    context = {
        'profile': profile,
        'cars': cars,
    }

    return render(request, 'car/catalogue.html', context)


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-create.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CarDetailsView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'car'


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car/car-create.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('catalog')


#
# def car_delete(request):
#     return render(request, 'car/car-delete.html')
#

class CarDeleteView(DeleteView):
    model = Car
    form_class = CarDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'car/car-delete.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
