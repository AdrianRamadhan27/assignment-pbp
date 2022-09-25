from importlib.resources import path
from django.urls import path
from todolist.views import delete_task, show_todolist, register, login_user, logout_user, create_task, update_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete/<id>', delete_task, name='delete_task'),
    path('update/<id>', update_task, name='update_task'),
]