from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('index/', views.index, name='index'),
    url('register/', views.register, name='register'),
    url('profile/', views.profile, name='profile'),
    url('login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'),
    url('logout/',
        auth_views.LogoutView.as_view(template_name='logout.html'),
        name='logout'),
    url('', PostListView.as_view(), name='index'),
    url('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
