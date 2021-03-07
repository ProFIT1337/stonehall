from django.urls import path

from administration.views import AdministrationBaseView, NewPostView, FeedbackView, FeedbackAnsweredView

urlpatterns = [
    path('', AdministrationBaseView.as_view(), name='administration_base'),
    path('новый-пост/', NewPostView.as_view(), name='administration_new_post'),
    path('фидбек/', FeedbackView.as_view(), name='administration_feedback'),
    path('фидбек-отвечено/<int:pk>/', FeedbackAnsweredView.as_view(), name='administration_feedback_answered'),

]