from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic
from .forms import MyForm

# シンプルにHTML形式の文字列を返すだけ
def index(request):
    return HttpResponse("<h1>attr_test</h1>")

class MyView(generic.FormView):
    template_name = "add_attr/my_template.html"
    form_class = MyForm

