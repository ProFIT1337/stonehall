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
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('remove-cache/', clear_cache, name='delete_cache'),
    path('new-post/', NewPostView.as_view(), name='administration_new_post'),
    path('edit-post/', EditPostView.as_view(), name='administration_edit_post'),
    path('edit-specific-post/<int:pk>/', EditSpecificPostView.as_view(), name='administration_edit_specific_post'),
    path('remove-post/', DeletePostView.as_view(), name='administration_delete_post'),
    path('remove-specific-post/<int:pk>/', DeleteSpecificPostView.as_view(),
         name='administration_delete_specific_post'),
    path('image-list/', ImagesListView.as_view(), name='administration_images_list'),
    path('add-image/', NewImageView.as_view(), name='administration_add_image'),
    path('remove-image/<int:pk>/', ImageDeleteView.as_view(), name='administration_delete_image'),
    path('edit-image/<int:pk>/', ImageEditView.as_view(), name='administration_edit_image'),
    path('feedback/', FeedbackView.as_view(), name='administration_feedback'),
    path('feedback-answered/<int:pk>/', FeedbackAnsweredView.as_view(), name='administration_feedback_answered'),
    path('remove-feedback/<int:pk>/', FeedbackDeleteView.as_view(), name='administration_feedback_delete'),
]
