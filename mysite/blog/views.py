from django.shortcuts import render
from django.utils import timezone
from blog.models import Post, comments
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
class AboutView(TemplateView):
    template_name = "about.html"


class postListView(ListView):
    model = post

    def get_queryset(self):
        return post.objects.filter(published_date__lte=timezone.now()).order_by(
            "-published_date"
        )


class postDetailView(DetailView):

    model = Post
