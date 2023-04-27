from django.urls import path
from . import views

app_name = "app_ft" # HTMLで参照するときに名前空間で識別
urlpatterns = [
    path("", views.index, name="index"),
    path("input/", views.UserInputFormView.as_view(), name="input"),
    path("confirm/", views.UserConfirmFormView.as_view(), name="confirm"),
]

