from django.urls import path
from . import views

app_name = "conf" # HTMLで参照するときに名前空間で識別
urlpatterns = [
    path("", views.index, name="index"),
    path("inquiry1", views.Inquiry1View.as_view(), name="inquiry1"),
    path("inquiry2", views.Inquiry2View.as_view(), name="inquiry2"),
    path("confirm1", views.Confirm1View.as_view(), name="confirm1"),
    path("complete", views.CompleteView.as_view(), name="complete"),
]
