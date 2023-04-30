# Django official tutorial

- https://docs.djangoproject.com/ja/4.2/intro/tutorial01/

## create project

```sh
django-admin startproject mysite
cd mysite
python manage.py runserver
```

## add app

```sh
python manage.py startapp polls
```

1. polls/urls.pyの追加
2. mysite/urls.pyへルーティング追加
3. polls/views.pyに関数実装

```sh
python manage.py runserver
```
http://127.0.0.1:8000/polls/ へ接続


## create db

```sh
python manage.py migrate
```

1. polls/model.pyにモデルを実装
2. mysite/settings.pyのINSTALLED_APPSにappを追加

```sh
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001 # 中身確認するだけ
python manage.py migrate
```

## 管理ユーザーを追加

```sh
python manage.py createsuperuser
    Username: admin
    Email address: admin@example.com
    Password: **********
    Password (again): *********

python manage.py runserver
```

http://127.0.0.1:8000/admin/ で管理画面に入れる

1. polls/admin.py にappモデルの登録処理を実装

## FormClass

### Field

- [【Django】forms.py：フォームのフィールドの種類（型）と引数一覧 | OFFICE54](https://office54.net/python/django/forms-field-argument#section3-3)
- [【Django】ChoiceFiledでラジオボタンを横並びに出力する方法(ulとli要素を除外して描画) - nobu blog](https://nobunobu1717.site/?p=1867)

## View

### Formview

- https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/


#### 任意のデータを追加

- [【django】get_context_dataの使い方とコンテキスト情報の取り扱い方法 | みかん箱でプログラミング](https://en-junior.com/get_context_data/)


## Tips

### vscode拡張機能
- [【Django】テンプレートのVSCode拡張をどれにするか悩む - PUROGU LADESU](https://puroguradesu.hatenadiary.jp/entry/2021/02/27/144912)

### html上で属性を追加

- [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)


### classなどの属性をformsに追加

```python
from django import forms

class MyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'my-class my-class2'
            field.widget.attrs['foo'] = '3'
        # 任意のfieldに属性を追加できる
        self.fields['name'].widget.attrs['name-attr'] = '1'
```

### validationチェック

#### formsでやる場合

formsで入力値をチェックするので，次ページに遷移する前にチェックできる

```python
from django import forms

class EmailForm(forms.Form):
    email_1 = forms.EmailField(label="メールアドレス1")
    email_2 = forms.EmailField(label="メールアドレス2")

    def clean(self):
        cleaned_data = super().clean()
        email_1 = cleaned_data.get("email_1")
        email_2 = cleaned_data.get("email_2")

        if 'admin' in email_1 and 'admin' in email_2:
            # forms.ValidationErrorはフォーム画面の上部にエラーを出す
            # raise forms.ValidationError("adminを含んだメールアドレスは使えません")

            # フィールドごとにメッセージを出す場合
            self.add_error("email_1", "adminを含んだメールアドレスは使えません")
            self.add_error("email_2", "adminを含んだメールアドレスは使えません")
```

#### viewsでやる場合

viewsはpostやgetされてきたものに対してチェックをかけて，問題があったら前ページにリダイレクトさせる

```python

```

### urlの逆参照の記法

#### 引数があるURLの場合

htmlの場合は後ろに引数の数だけスペース区切りで指定する．

実在するメンバを指定しないと起動時にエラーになるため，注意．

```html
<form action="{% url 'app:hoge' data.id %}" method="post">
```


```python
reverse('app:foo', args=[pk])
# or
reverse('app:foo', kwargs={'pk':pk})

# reverse('testtest:index_redirect', kwargs={'is_run': is_run})
```


