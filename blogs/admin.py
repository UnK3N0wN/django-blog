from django.contrib import admin
from .models import Category
from .models import Blog, Comment, Report

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('post', 'reported_by', 'reason', 'created_at')
    list_filter = ('reason', 'created_at')
    search_fields = ('post__title', 'reported_by__username', 'reason')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Report, ReportAdmin)