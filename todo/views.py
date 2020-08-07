from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import item

def index(request):
    all_items = item.objects.all()
    #return HttpResponse("dggdg")  # this is for common response
    return render(request,'todo.html', {'all':all_items})  # render is to request html page

def addtodo(request):
    #c = request.POST['content']
    new_item = item(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
    #once create a new todo all
    # save
    # redirect

def deletetodo(request, todo_id):
    item_to_delete = item.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
