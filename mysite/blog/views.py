from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post, Comment
from .forms import postForm, commentsForm
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"


class postListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by(
            "-published_date"
        )


class postDetailView(DetailView):

    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = postForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    redirect_field_name = "blog/post_detail.html"
    form_class = postForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("post_lazy")
    model = Post


class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    redirect_field_name = "blog/post_list.html"
    model = Post

    def get_queryset(self):
        return post.objects.filter(published_date__isnull=True).order_by(
            "-published_date"
        )


#################################################
# post
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect("post_detail", pk=pk)


# comments
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = commentsForm(request.POST)
        if form_isvalid():
            comment = form.save(commit=False)
            comment.Post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)

        else:
            form = commentsForm()

        return render(request, "blog/comment_form.html", {"form": form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect("post_detail", pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("post_detail", pk=post_pk)
