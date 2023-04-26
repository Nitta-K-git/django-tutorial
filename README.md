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



