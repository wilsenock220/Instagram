from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
