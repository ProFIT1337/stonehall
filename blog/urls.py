from django.urls import path, include
from django.views.decorators.cache import cache_page

from blog.views import BaseView, AboutView, PostListView, ContactView, LoginView

urlpatterns = [
    path('', cache_page(24 * 60)(BaseView.as_view()), name='base'),
    path('о-нас/', AboutView.as_view(), name='about'),
    path('проекты/', cache_page(24 * 60)(PostListView.as_view()), name='projects'),
    path('контакты/', ContactView.as_view(), name='contact'),
    path('логин/', LoginView.as_view(), name='login'),
    path('администрирование/', include('administration.urls'))

]
