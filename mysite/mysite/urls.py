from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("polls2/", include("polls2.urls")),
    path("fv/", include("formview_sample.urls")),
    path("ft/", include("form_tag.urls")),
    path("register/", include("register.urls")),
    path("admin/", admin.site.urls),
]
