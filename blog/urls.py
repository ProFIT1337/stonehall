from django.urls import path

from blog.views import BaseView, PostDetailView, AboutView, PostListView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('пост/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('о-нас/', AboutView.as_view(), name='about'),
    path('проекты/', PostListView.as_view(), name='projects'),
]

# projects проекты
# contacts - контакты