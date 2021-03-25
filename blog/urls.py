from django.urls import path, include

from blog.views import BaseView, AboutView, PostListView, ContactView, LoginView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('about/', AboutView.as_view(), name='about'),
    path('projects/', PostListView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('administration/', include('administration.urls'))

]
