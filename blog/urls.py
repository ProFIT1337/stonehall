from django.urls import path

from blog.views import BaseView, PostDetailView, AboutView, PostListView, ContactView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('пост/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('о-нас/', AboutView.as_view(), name='about'),
    path('проекты/', PostListView.as_view(), name='projects'),
    path('контакты/', ContactView.as_view(), name='contact'),
]

# projects проекты
# contacts - контакты