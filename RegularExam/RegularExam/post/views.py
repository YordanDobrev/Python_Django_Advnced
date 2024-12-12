from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView

from RegularExam.post.forms import PostCreateForm, PostUpdateForm, PostDeleteForm
from RegularExam.post.models import Post
from RegularExam.utils import get_user_obj


def dashboard(request): #TRY TO FIX THE DASHBOARD
    profile = get_user_obj()
    posts = Post.objects.all()

    context = {
        'profile': profile,
        'posts': posts,
    }

    return render(request, 'dashboard.html', context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'post/delete-post.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'post/edit-post.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'id'


class PostDetailsView(DetailView):
    model = Post
    template_name = 'post/details-post.html'
    pk_url_kwarg = 'id'
