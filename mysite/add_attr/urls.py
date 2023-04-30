from django.urls import path
from . import views

app_name = "add_attr" # HTMLで参照するときに名前空間で識別
urlpatterns = [
    path("", views.index, name="index"),
    path("myview", views.MyView.as_view(), name="myview"),
]
