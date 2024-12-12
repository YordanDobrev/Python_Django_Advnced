from datetime import datetime

from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView, RedirectView

from ForumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from ForumApp.posts.models import Post


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

    """
    OLD Index Logic
    
    def index(request):
        post_form = modelform_factory(
            Post,
            fields=('title', 'content', 'author', 'languages'),
        )
    
        context = {
            "my_form": post_form,
        }
    
        return render(request, 'common/index.html', context)
    """


class DashboardView(ListView):
    model = Post
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm

    def get_queryset(self):
        queryset = self.model.objects.all()

        if "query" in self.request.GET:
            query = self.request.GET.get("query")
            queryset = self.queryset.filter(title__icontains=query)

        return queryset


def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data['query']
            posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, 'posts/dashboard.html', context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dash')
    """
    OLD Create Logic
    
    def add_post(request):
    form = PostCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dash')

    context = {
        "form": form,
    }

    return render(request, 'posts/add-post.html', context)
    """


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')

    """
    OLD Edi Logic
    
    def edit_post(request, pk: int):
        post = Post.objects.get(pk=pk)
    
        if request.method == 'POST':
            form = PostEditForm(request.POST, instance=post)
    
            if form.is_valid():
                form.save()
                return redirect('dash')
        else:
            form = PostEditForm(instance=post)
    
        context = {
            "form": form,
            "post": post,
        }
    
        return render(request, 'posts/edit-post.html', context)
    """


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

    context = {
        "post": post,
        "formset": formset,
    }

    return render(request, 'posts/details-post.html', context)


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__

    """
    OLD Delete Logic
    
    def delete_post(request, pk: int):
        post = Post.objects.get(pk=pk)
        form = PostDeleteForm(instance=post)
    
        if request.method == "POST":
            post.delete()
            return redirect('dash')
    
        context = {
            "form": form,
            "post": post,
        }
    
        return render(request, 'posts/delete-post.html', context)
    """


class RedirectHomeView(RedirectView):
    url = reverse_lazy('index')