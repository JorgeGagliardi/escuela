from django.shortcuts import render


# Create your views here.
def home(request):
    return render (request,"entidades/index.html")

def cursos(request):
    return render (request,"entidades/cursos.html")

def profesores(request):
    return render (request,"entidades/profesores.html")

def estudiantes(request):
    return render (request,"entidades/estudiantes.html")

def tp(request):
    return render (request,"entidades/tp.html")
