from django.urls import path

from blog.views import BaseView

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
]