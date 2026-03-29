from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseForbidden
from assignments.models import About
from blogs.models import Blog, Category, Report
from django.contrib.auth.decorators import login_required
from .forms import AddUserForm, BlogPostForm, CategoryForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('home')

    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    return render(request, 'dashboard/dashboard.html', {
        'category_count': category_count,
        'blogs_count': blogs_count,
    })

def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required
def add_category(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Not allowed")
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

@login_required
def edit_category(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Not allowed")
    
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)

@login_required
def delete_category(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Not allowed")
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

@login_required
def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)

@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Temporarily save the form data
            post.author = request.user  # Set the author to the currently logged-in user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id)# Generate slug from the title
            post.save()  # Save the post with the slug
            return redirect('posts')
        else:
            print(form.errors)
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)

@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    # Only allow the author of the post to edit
    if request.user != post.author:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()

            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-'+str(post.id) # Generate slug from the title
            post.save()  # Save the post with the slug

            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)

@login_required
def delete_post(request, pk):

    post = get_object_or_404(Blog, pk=pk)

    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden("You cannot delete this post")

    post.delete()

    messages.success(request, "Post deleted successfully.")

    return redirect('posts')

@login_required
def my_posts(request):
    posts = Blog.objects.filter(author=request.user).order_by('-created_at')

    context = {
        'posts': posts
    }

    return render(request, 'dashboard/my_posts.html', context)

@login_required
def report_post(request, pk):

    post = get_object_or_404(Blog, pk=pk)

    # Prevent reporting own post
    if request.user == post.author:
        messages.error(request, "You cannot report your own post.")
        return redirect('posts')

    # Prevent duplicate report
    if Report.objects.filter(post=post, reported_by=request.user).exists():
        messages.warning(request, "You have already reported this post.")
        return redirect('posts')

    if request.method == "POST":
        reason = request.POST.get("reason")

        # Create report with reason
        Report.objects.create(
            post=post,
            reported_by=request.user,
            reason=reason
        )

        messages.success(request, "Post reported successfully.")

        # Notify admins
        admins = User.objects.filter(is_superuser=True)

        for admin in admins:
            print(f"Notify admin: {admin.username} about reported post '{post.title}'")

    return redirect('posts')

def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'dashboard/users.html', context)

@login_required
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUserForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_user.html', context)

@login_required
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/edit_user.html', context)

@login_required
def delete_user(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Not allowed")

    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users')

