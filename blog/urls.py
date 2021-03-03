from django.urls import path

from blog.views import BaseView, CategoryDetailView, PostDetailView, AboutView, ProjectsView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('категория/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('пост/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('о-нас/', AboutView.as_view(), name='about'),
    path('проекты/', ProjectsView.as_view(), name='projects')
]

# projects проекты
# contacts - контакты