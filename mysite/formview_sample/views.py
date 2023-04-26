from .forms import ContactForm
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Author

def index(request):
    return HttpResponse("fv test")

def thanks(request):
    return HttpResponse("thanks!!")

class ContactFormView(FormView):
    template_name = "formview_sample/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("app_fv:thanks")

    # 静的な追加のコンテキストを渡したい場合はこの変数にdict設定
    extra_context = {"extra": "This is an extra context."}

    # 動的な値を設定したい場合はこっち
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        extra = {"extra2": "動的に追加したデータ"}
        context.update(extra)
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class AuthorCreateView(CreateView):
    model = Author
    fields = ["name", "age"]
    template_name = "formview_sample/author_form.html"
    success_url = reverse_lazy("app_fv:list")


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ["name", "age"]
    template_name_suffix = "_update_form"


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy("author-list")


class AuthorDetailView(DeleteView):
    model = Author
    template_name = "formview_sample/author_detail.html"


class AuthorListView(ListView):
    model = Author
    template_name = "formview_sample/author_list.html"
