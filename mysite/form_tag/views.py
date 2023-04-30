from typing import Any, Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views import generic

from .form import UserInputForm, UserConfirmForm

# シンプルにHTML形式の文字列を返すだけ
def index(request):
    return HttpResponse("<h1>form tag sample</h1>")

class UserInputFormView(generic.FormView):
    template_name = "form_tag/user_input_form.html"
    form_class = UserInputForm
    success_url = reverse_lazy("app_ft:confirm")

    def form_valid(self, form):
        form.form_func()
        return super().form_valid(form)

class UserConfirmFormView(generic.FormView):
    template_name = "form_tag/user_confirm_form.html"
    form_class = UserInputForm
    # success_url = reverse_lazy("app_ft:index")

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     print("form", form)
    #     if not form.is_valid():
    #         return HttpResponseRedirect(reverse_lazy('app_ft:index'))
    #     return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return render(self.request, 'form_tag/user_confirm_form.html', {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'form_tag/user_input_form.html', {'form': form})
