from Modelos.Estudiante import Estudiante
from Repositorios.RepositorioEstudiante import RepositorioEstudiante

class Controladorestudiante():
    def __init__(self):
        print("Creando Controlador Estudiante")
        self.repositorioEstudiante = RepositorioEstudiante()

    def crear(self, infoEstudiante):
        print("Crear un estudiante")
        estudiantes = Estudiante(infoEstudiante)
        return self.repositorioEstudiante.save(estudiantes)

    def mostrarEstudiante(self, id):
        print("Mostrando el estudiante con id: "+id)
        estudiantes = Estudiante(self.repositorioEstudiante.findById(id))
        return estudiantes.__dict__

    def mostrarEstudiantes(self):
        print("Mostrando todos los estudiantes")
        return self.repositorioEstudiante.findAll()

    def actualizar(self,id,infoEstudiante):
        print("Actualizando el estudiante con id: "+id)
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula = infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)

    def eliminar(self,id):
        print("eliminando el estudiante con id: "+id)
        return self.repositorioEstudiante.delete(id)
