from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, ListView

from blog.forms import LoginForm
from blog.models import Post
from blog.services import get_posts_for_main_page, save_question_to_db, login_user_to_site
from question.forms import QuestionForm


class BaseView(View):
    """Main page view"""

    def get(self, request, *args, **kwargs):
        main_posts = get_posts_for_main_page()
        form = QuestionForm()
        context = {
            'posts': main_posts,
            'form': form,
        }
        return render(request, 'base.html', context)


class AboutView(View):
    """View with information about firm"""

    def get(self, request, *args, **kwargs):
        form = QuestionForm()
        context = {
            'form': form
        }
        return render(request, 'about.html', context)


class ContactView(View):
    """View with contact information"""

    def get(self, request, *args, **kwargs):
        form = QuestionForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        bound_form = QuestionForm(request.POST)
        if bound_form.is_valid():
            save_question_to_db(request, bound_form)
            return HttpResponseRedirect('/контакты')
        context = {
            'form': bound_form,
        }
        return render(request, 'contact.html', context)


class PostListView(ListView):
    """View with all posts"""
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    form = QuestionForm()

    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context


class LoginView(View):
    """View with user login form"""

    def get(self, request, *args, **kwargs):
        """When login page is called by method GET"""
        form = LoginForm(request.POST or None)
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        """When login page is called by method POST"""
        form = LoginForm(request.POST or None)
        if form.is_valid():
            if login_user_to_site(request, form):
                return HttpResponseRedirect('/')
        return render(request, 'login.html', {'form': form})
