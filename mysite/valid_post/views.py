from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreateForm

class UserList(generic.ListView):
    template_name = 'valid_post/user_list.html'  # デフォルトUserだと、authアプリケーションのuser_list.htmlを探すため、明示的に書いておく

class UserDataInput(generic.FormView):
    template_name = 'valid_post/user_data_input.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        return render(self.request, 'valid_post/user_data_input.html', {'form': form})


class UserDataConfirm(generic.FormView):
    form_class = UserCreateForm

    def post(self, request, *args, **kwargs):
        print("post-------------")
        context = self.get_context_data(**kwargs)
        form = context["form"]  # contextはformとviweのオブジェクトをdictで持っている
        print(form.data.dict()["name"])  # validが評価されていないため，cleaned_dataはまだ使えない
        if form.is_valid():
            print(form.cleaned_data["name"])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):  # formにはform_classで指定した型のオブジェクトが入る
        print("form_valid-------------")
        name = form.cleaned_data["name"]  # 辞書型でデータにアクセスできる
        print("form.cleaned_data", form.cleaned_data)
        print("form.data.dict()", form.data.dict())
        non_form_text = form.data.dict()["non_form_text"]  # form_classにない要素はこっちで取得する

        return render(self.request, 'valid_post/user_data_confirm.html', {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'valid_post/user_data_input.html', {'form': form})


class UserDataCreate(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('valid_post:user_list')

    def form_invalid(self, form):
        return render(self.request, 'valid_post/user_data_input.html', {'form': form})
