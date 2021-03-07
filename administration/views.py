from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View

from administration.forms import NewPostForm


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

