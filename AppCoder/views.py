from django.shortcuts import render
from django.http import HttpResponse
from .models import Profesor, Curso
from .forms import ProfesorFormulario

# Create your views here.
"""
def profe_nuevo(request):
    profeN = Profesor(nombre="Pepe", apellido="Python", email="pepe@python.com", profesion="Biofisico")
    profeN.save()

    return HttpResponse(f"Hemos guardado al profesor {profeN.nombre}")


def curso_nuevo(request):
    mi_curso_favorito = Curso(nombre="Python", comision=47765)
    mi_curso_favorito.save()

    return HttpResponse(f"Bienvenidos al curso {mi_curso_favorito.nombre}")
"""

def inicio(request):
    nombre = "Pepe"
    return render(request, "AppCoder/inicio.html", {"name":nombre}) #3er argumento: contexto



def ver_entregras(request):
    return render(request, "AppCoder/ver_entregas.html")

def ver_estudiante(request):
    return render(request, "AppCoder/ver_estudiantes.html")

def crear_cursos(request):
    if request.method == "POST": #al presionar el botón
        curso_nuevo = Curso(nombre=request.POST["nombre"], comision=request.POST["comision"])
        curso_nuevo.save()
        return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/crear_cursos.html")



def buscar_profes(request):

    return render(request, "AppCoder/buscar_profes.html")

def resultado_profes(request):

    if request.GET["apellido"]: #cuando hagamos click al botón y hay datos

        apellido = request.GET["apellido"] #valor que introduje en el cuadrito de búsqueda
        profes_resultado = Profesor.objects.filter(apellido__icontains=apellido) #buscar un match entre los datos que ya tengo

        return render(request, "AppCoder/resultado_profes.html", {"valor":apellido, "res":profes_resultado})

    else: #si hacemos click al botón sin datos!!!!
        return HttpResponse("No enviaste datos.")

    return render(request, "AppCoder/resultado_profes.html")





#HACIENDO EL CRUD de Profes --- CLÁSICO

#Read
def ver_profes(request):

    todos = Profesor.objects.all()

    return render(request, "AppCoder/ver_profes.html", {"profes":todos})

#Create
def crear_profes(request):
 
    if request.method == "POST": #hacemos click al botón enviar

        miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html 

        if miFormulario.is_valid():
                info = miFormulario.cleaned_data
                profe_nuevo = Profesor(nombre=info["nombre"], apellido=info["apellido"], 
                                    email=info["email"],profesion =info["profesion"])
                profe_nuevo.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = ProfesorFormulario() #mostramos formulario vacío

        return render(request, "AppCoder/crear_profes.html", {"form": miFormulario})
    

def eliminar_profesor(request, profesor_nombre):

    profesor_escogido = Profesor.objects.get(nombre=profesor_nombre)
    profesor_escogido.delete()
    todos = Profesor.objects.all()

    return render(request,"AppCoder/ver_profes.html", {"profes":todos} )







def actualizar_profesor(request, profesor_nombre):
    pass





#HACIENDO EL CRUD de Profes --- CLÁSICO

#Read
def ver_cursos(request):
    todos = Curso.objects.all()
    return render(request, "AppCoder/ver_cursos.html", {"cursos":todos})
