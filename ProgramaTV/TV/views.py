from django.shortcuts import render, redirect
from TV.models import Libro
from django.contrib import messages
from time import gmtime, strftime
from datetime import datetime

def new(request):
    return render(request, "index.html")

def create(request):
    error=Libro.objects.validacion_new(request.POST)
    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
            print(key, value)
        return redirect('/shows/new')
    else:
        op = Libro.objects.create(title=request.POST['titulo_1'], netword=request.POST['net_1'], release_date=request.POST['fecha_1'], description=request.POST['desc'])
        return redirect(f'/shows/{op.id}')
# Create your views here.

def show(request):
    libro=Libro.objects.all()
    export=[]
    for u in libro:
        export.append({'id': u.id, 'titulo': u.title, 'Network': u.netword, "Fecha de Estreno": u.release_date})

    context = {
        'libros': export
    }
    return render(request, "show_all.html", context)

def update(request,op):
    error=Libro.objects.validacion(request.POST)
    if len(error)>0:
        for key, value in error.items():
            messages.error(request, value)
            print(key, value)
        return redirect(f'/shows/{op}/edit')
    else:
        libro = Libro.objects.get(id=int(op))
        libro.title = request.POST['titulo_1']
        libro.netword = request.POST['net_1']
        libro.release_date = request.POST['fecha_1']
        libro.description = request.POST['desc']
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
