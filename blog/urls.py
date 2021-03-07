from django.urls import path, include

from blog.views import BaseView, AboutView, PostListView, ContactView, LoginView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('о-нас/', AboutView.as_view(), name='about'),
    path('проекты/', PostListView.as_view(), name='projects'),
    path('контакты/', ContactView.as_view(), name='contact'),
    path('логин/', LoginView.as_view(), name='login'),
    # path('админинистрирование/', include(), name='admin')
]
