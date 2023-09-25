from django.urls import path
from .views import *

urlpatterns = [

    path("inicio/", inicio, name="Inicio"),

    #urls de leer
    path("cursos/", ver_cursos, name="VerCursos"),
    path("profes/", ver_profes, name="VerProfes"),
    path("entregas/", ver_entregras, name="VerEntregas"),
    path("estudiantes/", ver_estudiante, name="VerEstudiantes"),

    #urls de crear
    path("crear_curso/", crear_cursos, name="CrearCursos"),
    path("crear_profe/", crear_profes, name="CrearProfes"),

    #urls de búsqueda
    path("buscar_profe/", buscar_profes, name="BuscarProfes"),
    path("resu_profe/", resultado_profes, name="ResultadoProfes"),

    #urls de borrar
    path("borrar_profe/<profesor_nombre>", eliminar_profesor, name="BorrarProfe"),


]