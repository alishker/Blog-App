from django.urls import path
from blog import views
from blog.views import (
    AboutView,
    postListView,
    postDetailView,
    CreatePostView,
    PostUpdateView,
    PostDeleteView,
    DraftListView,
    comment_approve,
    comment_remove,
    post_publish,
    add_comment_to_post,
)


urlpatterns = [
    path("", postListView.as_view(), name="post_list"),
    path("about/$", AboutView.as_view(), name="about"),
    path("posts/<int:pk>/$", postDetailView.as_view(), name="post_detail"),
    path("posts/new/$", CreatePostView.as_view(), name="post_new"),
    path("posts/<int:pk>/update$", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete$", PostDeleteView.as_view(), name="post_remove"),
    path("draft/$", DraftListView.as_view(), name="post_draft_list"),
    path(
        "posts/<int:pk>/comment/$",
        views.add_comment_to_post,
        name="add_comment_to_post",
    ),
    path("comment/<int:pk>/approve/$", views.comment_approve, name="comment_approve"),
    path("comment/<int:pk>/remove/$", views.comment_remove, name="comment_remove"),
    path("post/<int:pk>/publish/$", views.post_publish, name="post_publish"),
]
