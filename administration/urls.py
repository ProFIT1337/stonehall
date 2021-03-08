from django.contrib.auth.views import LogoutView
from django.urls import path

from administration.views import \
    AdministrationBaseView, \
    NewPostView, \
    FeedbackView, \
    FeedbackAnsweredView, \
    EditPostView, \
    EditSpecificPostView, DeletePostView, DeleteSpecificPostView

urlpatterns = [
    path('', AdministrationBaseView.as_view(), name='administration_base'),
    path('выйти/', LogoutView.as_view(next_page='/'), name='logout'),
    path('новый-пост/', NewPostView.as_view(), name='administration_new_post'),
    path('фидбек/', FeedbackView.as_view(), name='administration_feedback'),
    path('фидбек-отвечено/<int:pk>/', FeedbackAnsweredView.as_view(), name='administration_feedback_answered'),
    path('изменить-пост/', EditPostView.as_view(), name='administration_edit_post'),
    path('изменить-конкретный-пост/<int:pk>', EditSpecificPostView.as_view(), name='administration_edit_specific_post'),
    path('удалить-пост/', DeletePostView.as_view(), name='administration_delete_post'),
    path('удалить-конкретный-пост/<int:pk>', DeleteSpecificPostView.as_view(), name='administration_delete_specific_post'),

]