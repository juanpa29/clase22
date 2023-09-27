from django.urls import path
from .views import *

urlpatterns = [

    path("inicio/", inicio, name="Inicio"),

    #urls de leer
    path("cursos/", ver_cursos, name="VerCursos"),
    path("entregas/", ver_entregras, name="VerEntregas"),
    path("estudiantes/", ver_estudiante, name="VerEstudiantes"),

    #urls de crear
    path("crear_curso/", crear_cursos, name="CrearCursos"),

    #urls de búsqueda
    path("resu_profe/", resultado_profes, name="ResultadoProfes"),

    #urls de borrar

    #CRUD de profesor
    path("profes/", ver_profes, name="VerProfes"),
    path("buscar_profe/", buscar_profes, name="BuscarProfes"),
    path("crear_profe/", crear_profes, name="CrearProfes"),
    path("borrar_profe/<profesor_nombre>", eliminar_profesor, name="BorrarProfe"),
    path("update_profe/<profesor_nombre>", actualizar_profesor, name="Actualizar Profesor"),


    #CRUD de estudiante con vistas usando Clases
    path("estudiantes/lista/", EstudianteLista.as_view(), name="Ver Estudiantes"),
    path("estudiantes/detalle/<int:pk>", EstudianteDetalle.as_view(), name="Detalle Estudiantes"),
    path("estudiantes/nuevo/", EstudianteCrear.as_view(), name="Crear Estudiantes"),
    path("estudiantes/actualizar/<int:pk>", EstudianteActualizar.as_view(), name="Actualizar Estudiantes"),
    path("estudiantes/borrar/<int:pk>", EstudianteBorrar.as_view(), name="Borrar Estudiantes"),


    path("login/", login_view, name="Inicio Sesion"),
]