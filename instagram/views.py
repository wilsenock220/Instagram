from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'index.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please login !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')