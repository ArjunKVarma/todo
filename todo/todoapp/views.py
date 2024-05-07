from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Todo

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        # Ensure password matches confirmation
        password = request.POST["password"]
       
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, password)
            user.save()
        except IntegrityError:
            return render(request, "registration/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, 'registration/register.html')
    


def sign_in(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "registration/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "registration/login.html")
    
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


@login_required(login_url='/login')
def home(request):
    todos = Todo.objects.filter(owner= request.user)
    ctodos = todos.filter(complete=True)
    ptodos = todos.filter(complete=False)
    return render(request, 'todoapp/home.html', {
        'ctodos': ctodos,
        'ptodos' : ptodos
    })


@login_required(login_url='/login')
def new(request):
    
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        enddate = request.POST.get('endDate')
        new_task = Todo.objects.create(title=title, content=content, enddate=enddate, owner= request.user)
        new_task.save()
        return redirect('home')
    return render(request, 'todoapp/new.html')


@login_required(login_url='/login')
def edit(request, id):
    if request.method =="POST":
        todo = Todo.objects.get(id=id)
        todo.titie = request.POST['title']
        todo.content = request.POST['content']

        todo.save()
        return HttpResponseRedirect(reverse(home))
    
    todo = Todo.objects.get(id=id)
   
    return render(request, 'todoapp/edit.html',{
        'todo' : todo
    })


@login_required(login_url='/login')
def complete(request,id):
    todo = Todo.objects.get(id=id)
    todo.complete = True
    todo.save()
    return HttpResponseRedirect(reverse(home))