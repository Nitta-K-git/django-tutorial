from django.urls import path
from . import views

app_name = "app_fv" # HTMLで参照するときに名前空間で識別
urlpatterns = [
    path("", views.index, name="fv"),
    path("contact/", views.ContactFormView.as_view(), name="fv-contact"),
    path("thanks/", views.thanks, name="thanks"),
    path("create/", views.AuthorCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.AuthorUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", views.AuthorDeleteView.as_view(), name="delete"),
    path("detail/<int:pk>", views.AuthorDetailView.as_view(), name="detail"),
    path("list/", views.AuthorListView.as_view(), name="list"),
]
