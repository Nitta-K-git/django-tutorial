from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreateForm

User = get_user_model()


class UserList(generic.ListView):
    template_name = 'register/user_list.html'  # デフォルトUserだと、authアプリケーションのuser_list.htmlを探すため、明示的に書いておく
    model = User


class UserDataInput(generic.FormView):
    """ユーザー情報の入力

    このビューが呼ばれるのは、以下の2箇所です。
    ・初回の入力欄表示(aタグでの遷移)
    ・確認画面から戻るを押した場合(これはPOSTで飛んできます)

    初回の入力欄表示の際は、空のフォームをuser_data_input.htmlに渡し、
    戻る場合は、POSTで飛んできたフォームデータをそのままuser_data_input.htmlに渡します。

    """
    template_name = 'register/user_data_input.html'
    form_class = UserCreateForm

    def form_valid(self, form):
        return render(self.request, 'register/user_data_input.html', {'form': form})


class UserDataConfirm(generic.FormView):
    """ユーザー情報の確認

    ユーザー情報入力後、「送信」を押すとこのビューが呼ばれます。(user_data_input.htmlのform action属性がこのビュー)
    データが問題なければuser_data_confirm.html(確認ページ)を、入力内容に不備があればuser_data_input.html(入力ページ)に
    フォームデータを渡します。

    """
    form_class = UserCreateForm

    def form_valid(self, form):
        return render(self.request, 'register/user_data_confirm.html', {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'register/user_data_input.html', {'form': form})


class UserDataCreate(generic.CreateView):
    """ユーザーデータの登録ビュー。ここ以外では、CreateViewを使わないでください"""
    form_class = UserCreateForm
    success_url = reverse_lazy('register:user_list')

    def form_invalid(self, form):
        """基本的にはここに飛んでこないはずです。UserDataConfrimでバリデーションは済んでるため"""
        return render(self.request, 'register/user_data_input.html', {'form': form})
