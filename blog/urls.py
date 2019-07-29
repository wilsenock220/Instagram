from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
   url('', PostListView.as_view(), name='blog-home'),
   url('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
   url('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   url('post/new/', PostCreateView.as_view(), name='post-create'),
   url('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
   url('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   url('about/', views.about, name='blog-about'),
]
