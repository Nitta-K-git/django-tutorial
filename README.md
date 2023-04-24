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

## ビューの追加・拡張

- 引数を取るビュー
