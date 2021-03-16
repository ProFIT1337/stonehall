from django.contrib.auth.views import LogoutView
from django.urls import path

from administration.views import \
    AdministrationBaseView, \
    NewPostView, \
    FeedbackView, \
    FeedbackAnsweredView, \
    EditPostView, \
    EditSpecificPostView, \
    DeletePostView, \
    DeleteSpecificPostView, \
    FeedbackDeleteView, \
    ImagesListView, \
    ImageDeleteView, \
    ImageEditView, \
    NewImageView, \
    clear_cache

urlpatterns = [
    path('', AdministrationBaseView.as_view(), name='administration_base'),
    path('выйти/', LogoutView.as_view(next_page='/'), name='logout'),
    path('удалить-кэш/', clear_cache, name='delete_cache'),
    path('новый-пост/', NewPostView.as_view(), name='administration_new_post'),
    path('изменить-пост/', EditPostView.as_view(), name='administration_edit_post'),
    path('изменить-конкретный-пост/<int:pk>/', EditSpecificPostView.as_view(), name='administration_edit_specific_post'),
    path('удалить-пост/', DeletePostView.as_view(), name='administration_delete_post'),
    path('удалить-конкретный-пост/<int:pk>/', DeleteSpecificPostView.as_view(),
         name='administration_delete_specific_post'),
    path('список-фотографий/', ImagesListView.as_view(), name='administration_images_list'),
    path('добавить-фотографию/', NewImageView.as_view(), name='administration_add_image'),
    path('удалить-фотографию/<int:pk>/', ImageDeleteView.as_view(), name='administration_delete_image'),
    path('изменить-фотографию/<int:pk>/', ImageEditView.as_view(), name='administration_edit_image'),
    path('фидбек/', FeedbackView.as_view(), name='administration_feedback'),
    path('фидбек-отвечено/<int:pk>/', FeedbackAnsweredView.as_view(), name='administration_feedback_answered'),
    path('фидбек-удалить/<int:pk>/', FeedbackDeleteView.as_view(), name='administration_feedback_delete'),
]
