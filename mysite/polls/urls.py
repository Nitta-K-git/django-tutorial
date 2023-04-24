from django.urls import path
from . import views

app_name = "polls" # HTMLで参照するときに名前空間で識別
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/index02/
    path("index02/", views.index02, name="index02"),
    path("index03/", views.index03, name="index03"),
    path("index04/", views.index04, name="index04"),
    # ex: /polls/dummy5/
    path("dummy<int:question_id>/", views.detail_dummy, name="detail_dummy"),
    # ex: /polls/detail5/
    path("detail<int:question_id>/", views.detail_long, name="detail_long"),

    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
