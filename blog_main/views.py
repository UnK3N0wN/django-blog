from django.shortcuts import redirect, render
from django.contrib import messages
from assignments.models import About
from blogs.models import Blog, Category
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    # ✅ NOT logged in → show landing page
    if not request.user.is_authenticated:
        return render(request, 'landing.html')

    # ✅ Logged-in → show blog page
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')

    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }

    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '🎉 Account created successfully! Please login.')
            return redirect('login')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, f'👋 Welcome back, {user.username}!')

                # ✅ ROLE BASED REDIRECT
                if user.is_staff:
                    return redirect('dashboard')
                else:
                    return redirect('home')
            else:
                messages.error(request, '❌ Invalid username or password.')

        else:
            messages.error(request, '❌ Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.info(request, '👋 You have been logged out successfully.')
    return redirect('home')