from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.

def rav(reqest):
    ti = Todo.objects.all()
    context = {'ti':ti}
    
    return render(reqest,'index.html',context)

def create(reqest):
    pag = Todo()
    if reqest.method == 'POST':
        pag.title = reqest.POST.get('First_name')
        pag.descriptions = reqest.POST.get('Last_name')
        pag.save()
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def delete_record(reqest, id):
    paag = Todo.objects.get(id=id)
    paag.delete()
    return HttpResponseRedirect('/')


def update(reqest, id):
    paag = Todo.objects.get(id=id)
    if reqest.method == 'POST':
        paag.title = reqest.POST.get('title')
        paag.descriptions = reqest.POST.get('descriptions')
        paag.save()
        return HttpResponseRedirect('/')
    return render(reqest, 'update.html', {'paag':paag})

def anketa(reqest, id):
    paag = Todo.objects.get(id=id)
    return render(reqest, 'anketa.html', {'paag':paag})

   



