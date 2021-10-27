from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo

# Create your views here.
@csrf_exempt
def index(request):
    todo_items = Todo.objects.all().order_by("-date_added")
    return render(request, 'index.html', {'todo_items': todo_items})

@csrf_exempt
def add_todo(request):

    currentdate = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(date_added=currentdate, text=content)
    length_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')