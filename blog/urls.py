from django.urls import path

from blog.views import BaseView, CategoryDetailView, PostDetailView, AboutView


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('категория/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('пост/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('о-нас/', AboutView.as_view(), name='about'),
]

# projects проекты
# contacts - контакты