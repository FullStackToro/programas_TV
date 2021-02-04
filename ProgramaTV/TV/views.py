from django.shortcuts import render, redirect
from TV.models import Libro
from datetime import datetime

def new(request):
    return render(request, "index.html")

def create(request):
    op = Libro.objects.create(title=request.POST['t1'], netword=request.POST['c1'], release_date=request.POST['f1'], description=request.POST['d1'])
    return redirect(f'/shows/{op.id}')
# Create your views here.

def show(request):
    libro=Libro.objects.all()
    export=[]
    for u in libro:
        export.append({'id': u.id, 'titulo': u.title, 'Network': u.netword, "Fecha de Estreno": u.release_date})
        print(u.id, u.title, '\n'*2, '-'*40, '\n')

    context = {
        'libros': export
    }
    return render(request, "show_all.html", context)

def update(request,op):
    libro = Libro.objects.get(id=int(op))
    libro.netword=request.POST['n']
    libro.title=request.POST['t']
    libro.release_date=request.POST['f']
    libro.save()
    return redirect(f"/shows/{libro.id}")


def edit(request, op):
    libro = Libro.objects.get(id=int(op))
    time = libro.release_date.strftime("%Y-%m-%d")
    context = {
        'id': libro.id,
        'network': libro.netword,
        'titulo': libro.title,
        'fecha': time,
        'descripcion': libro.description,
        'actualizado': libro.updated_at
    }
    return render(request, "edit.html", context)

def show_one(request, op):
    libro=Libro.objects.get(id=int(op))
    context={
        'id': libro.id,
        'network': libro.netword,
        'titulo': libro.title,
        'fecha': libro.release_date,
        'descripcion': libro.description,
        'actualizado': libro.updated_at
    }
    return render(request, "show_one.html", context)

def destroy(request, op):
    libro=Libro.objects.get(id=int(op))
    libro.delete()
    return redirect("/shows/")
