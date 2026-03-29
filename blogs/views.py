from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Blog, Category, Comment


# 🔹 Posts by category
def posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    posts = Blog.objects.filter(
        status='Published',
        category=category
    )

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


# 🔹 Single blog + comments
@login_required
def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')

    if request.method == 'POST':
        comment_text = request.POST.get('comment')

        if comment_text:  # ✅ prevent empty comments
            Comment.objects.create(
                user=request.user,
                blog=single_blog,
                comment=comment_text
            )

        return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(blog=single_blog).order_by('-id')

    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comments.count(),
    }
    return render(request, 'blogs.html', context)


# 🔹 Search
def search(request):
    keyword = request.GET.get('keyword', '')

    blogs = Blog.objects.none()

    if keyword:
        blogs = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status='Published'
        )

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)