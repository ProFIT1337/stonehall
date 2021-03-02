from django.contrib import admin

from blog.models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    """Admin class for model 'Category'"""
    prepopulated_fields = {'slug': ("name",)}


class PostAdmin(admin.ModelAdmin):
    """Admin class for model 'Post'"""
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
