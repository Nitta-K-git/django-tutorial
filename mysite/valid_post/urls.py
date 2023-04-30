# https://blog.narito.ninja/detail/45
from django.urls import path
from . import views

app_name = 'valid_post'

urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('user_data_input/', views.UserDataInput.as_view(), name='user_data_input'),
    path('user_data_confirm/', views.UserDataConfirm.as_view(), name='user_data_confirm'),
    path('user_data_create/', views.UserDataCreate.as_view(), name='user_data_create'),
]