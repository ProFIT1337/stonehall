from django.urls import path

from administration.views import \
    AdministrationBaseView, \
    NewPostView, \
    FeedbackView, \
    FeedbackAnsweredView, \
    EditPostView, \
    EditSpecificPostView

urlpatterns = [
    path('', AdministrationBaseView.as_view(), name='administration_base'),
    path('новый-пост/', NewPostView.as_view(), name='administration_new_post'),
    path('фидбек/', FeedbackView.as_view(), name='administration_feedback'),
    path('фидбек-отвечено/<int:pk>/', FeedbackAnsweredView.as_view(), name='administration_feedback_answered'),
    path('изменить-пост/', EditPostView.as_view(), name='administration_edit_post'),
    path('изменить-конкретный-пост/<int:pk>', EditSpecificPostView.as_view(), name='administration_edit_specific_post'),

]