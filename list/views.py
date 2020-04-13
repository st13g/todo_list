from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    todo_items = Todo.objects.all().order_by("-datet")
    return render(request,'list/main.html',{"todo_items":todo_items})

@csrf_exempt
def add_todo(request):
    currentdate = timezone.now()
    search = request.POST["content"]
    created=Todo.objects.create(datet=currentdate,text=search)

    return HttpResponseRedirect("/")
@csrf_exempt
def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect("/")
