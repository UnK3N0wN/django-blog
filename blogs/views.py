from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # Fetch posts that belong to category with id = category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # Use try/except when you want to do custom action if category does not exist
    #try:
    #    category = Category.objects.get(pk=category_id)
    #except:
        # redirect to home if category does not exist
    #    return redirect('home')
    
    # alternative to try except block is to use get_object_or_404 which will return 404 error if category does not exist
    category = get_object_or_404(Category, pk=category_id) 

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)