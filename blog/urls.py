from django.urls import path

from blog.views import BaseView, CategoryDetailView, PostDetailView


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('категория/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('пост/<str:slug>/', PostDetailView.as_view(), name='product_detail'),
]