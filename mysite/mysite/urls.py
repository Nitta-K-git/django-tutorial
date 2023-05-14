from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("polls2/", include("polls2.urls")),
    path("fv/", include("formview_sample.urls")),
    path("form_tag/", include("form_tag.urls")),
    path("register/", include("register.urls")),
    path("add_attr/", include("add_attr.urls")),
    path("valid_post/", include("valid_post.urls")),
    path("confirm/", include("confirm.urls")),

    path("admin/", admin.site.urls),
]
