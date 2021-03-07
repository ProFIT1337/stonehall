from django.urls import path

from administration.views import AdministrationBaseView, NewPostView

urlpatterns = [
    path('', AdministrationBaseView.as_view(), name='administration_base'),
    path('новый-пост/', NewPostView.as_view(), name='administration_new_post'),
]