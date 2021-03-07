from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View

from administration.forms import NewPostForm
from question.models import Question
from question.services import get_all_questions


class AdministrationBaseView(View):
    """Base view for administration page"""

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'administration_base.html', {})
        else:
            return redirect('login')


class NewPostView(View):
    """Administration view with adding new post"""

    def get(self, request, *args, **kwargs):
        form = NewPostForm(request.POST or None, request.FILES or None)
        context = {'form': form}
        return render(request, 'administration_new_post.html', context)

    def post(self, request, *args, **kwargs):
        form = NewPostForm(request.POST or None, request.FILES or None)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/администрирование')
        return render(request, 'administration_new_post.html', context)


class FeedbackView(View):
    """Administration view with feedback information"""

    def get(self, request, *args, **kwargs):
        questions = get_all_questions()
        context = {
            'questions': questions
        }
        return render(request, 'administration_feedback.html', context)


class FeedbackAnsweredView(View):
    """Endpoint for administration feedback form. Changes the value of the field is_answered?"""

    def post(self, request, *args, **kwargs):
        question_pk = kwargs.get('pk')
        question = Question.objects.get(pk=question_pk)
        is_answered = bool(request.POST.get('is_answered'))
        question.is_answered = is_answered
        question.save()
        return HttpResponseRedirect('/администрирование/фидбек')