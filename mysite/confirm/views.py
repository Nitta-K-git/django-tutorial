from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import Confirm1Form, Inquiry1Form, CompleteForm, Inquiry2Form

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. confirm</h1>")


# class UserList(generic.ListView):
#     template_name = 'register/user_list.html'  # デフォルトUserだと、authアプリケーションのuser_list.htmlを探すため、明示的に書いておく
#     model = User


class Inquiry1View(generic.FormView):
    """ユーザー情報の入力

    このビューが呼ばれるのは、以下の2箇所です。
    ・初回の入力欄表示(aタグでの遷移)
    ・確認画面から戻るを押した場合(これはPOSTで飛んできます)

    初回の入力欄表示の際は、空のフォームをuser_data_input.htmlに渡し、
    戻る場合は、POSTで飛んできたフォームデータをそのままuser_data_input.htmlに渡します。
    """
    template_name = 'confirm/inquiry1.html'
    form_class = Inquiry1Form

    # 次の画面から戻るときに走る
    def form_valid(self, form):
        print(self.__class__.__name__, "form valid")
        print(form)
        return render(self.request, self.template_name, {'form': form})


class Inquiry2View(generic.FormView):
    template_name = 'confirm/inquiry2.html'
    prev_template_name = 'confirm/inquiry1.html'
    
    form_class = Inquiry2Form

    # 次の画面から戻るときに走る
    def form_valid(self, form):
        print(self.__class__.__name__, "form valid")
        return render(self.request, self.template_name, {'form': form})


class Confirm1View(generic.FormView):
    """ユーザー情報の確認

    ユーザー情報入力後、「送信」を押すとこのビューが呼ばれます。(user_data_input.htmlのform action属性がこのビュー)
    データが問題なければuser_data_confirm.html(確認ページ)を、入力内容に不備があればuser_data_input.html(入力ページ)に
    フォームデータを渡します。

    """
    form_class = Confirm1Form
    template_name = "confirm/confirm1.html"
    prev_template_name = 'confirm/inquiry2.html'

    def form_valid(self, form):
        print(self.__class__.__name__, "form valid")
        return render(self.request, self.template_name, {'form': form})

    # https://yu-nix.com/archives/django-form-validation/
    def form_invalid(self, form):
        print(self.__class__.__name__, "form invalid")
        return render(self.request, self.prev_template_name, {'form': form})
    
    # 画面遷移で無く直接URL叩いたときにくる
    # 不正なので，エラーにすべき？
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print(self.__class__.__name__, "get")
        return super().get(request, *args, **kwargs)


class CompleteView(generic.FormView):
    form_class = CompleteForm
    template_name = "confirm/complete.html"
    prev_template_name = 'confirm/confirm1.html'

    def form_valid(self, form):
        print(self.__class__.__name__, "form valid")
        return render(self.request, self.template_name, {'form': form})

    def form_invalid(self, form):
        print(self.__class__.__name__, "form invalid")
        return render(self.request, self.prev_template_name, {'form': form})


# class UserDataCreate(generic.CreateView):
#     """ユーザーデータの登録ビュー。ここ以外では、CreateViewを使わないでください"""
#     form_class = UserCreateForm
#     success_url = reverse_lazy('register:user_list')

#     def form_invalid(self, form):
#         """基本的にはここに飛んでこないはずです。UserDataConfrimでバリデーションは済んでるため"""
#         return render(self.request, 'register/user_data_input.html', {'form': form})
