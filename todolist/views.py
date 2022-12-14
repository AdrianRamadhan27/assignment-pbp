from urllib.parse import parse_qs
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse
from todolist.models import Task
from todolist.forms import TaskForm
# Create your views here.

@login_required(login_url='/todolist/login')
def show_todolist(request):
    form = TaskForm(request.POST)

    # tasks = Task.objects.filter(user=request.user)
    context = {
        'username_login': request.COOKIES['user_name'],
        # 'tasks': tasks
        'form': form
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login')
def show_json(request):

    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account succesfully registered!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            response.set_cookie('user_name', username)
            return response
        else:
            messages.info(request, 'Username or Password Incorrect!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('user_name')

    return response

def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('todolist:show_todolist')

    context = {
        'form': form
    }
    return render(request, 'create_task.html', context)


def delete_task(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    data = {
            'deleted': True
        }
    return JsonResponse(data)

def update_task(request, id):
    task = Task.objects.get(id = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login')
def add_task_ajax(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(user=request.user, title=title, description=description)
        return JsonResponse({'error': False, 'msg':'Successful'})
    return redirect('todolist:show_todolist')    
