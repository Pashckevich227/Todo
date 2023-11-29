from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem


def todoView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_items})


def addTodoItem(request):
    content = request.POST['content']
    if content:
        new_item = TodoListItem(content=content)
        new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/todo/')
