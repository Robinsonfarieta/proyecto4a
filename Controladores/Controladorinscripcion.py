from Repositorios.RepositorioIncripcion import RepositorioInscripcion
from Repositorios.RepositorioEstudiante import RepositorioEstudiante
from Repositorios.RepositorioMateria import RepositorioMateria

from Modelos.Inscripcion import Inscripcion
from Modelos.Estudiante import Estudiante
from Modelos.Materia import Materia

class Controladorinscripcion():
    def __init__(self):
        print("Creando Controlador Inscripcion")
        self.repositorioInscripcion = RepositorioInscripcion()
        self.repositorioEstudiante = RepositorioEstudiante()
        self.repositorioMateria = RepositorioMateria()

    def crear(self,infoInscripcion, id_estudiante,id_materia):
        inscripcion = Inscripcion(infoInscripcion)
        estudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        materia = Materia(self.repositorioMateria.findById(id_materia))
        inscripcion.estudiante = estudiante
        inscripcion.materia = materia
        return self.repositorioInscripcion.save(inscripcion)

    def mostrarInscripcion(self, id):
        inscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return inscripcion.__dict__

    def mostrarInscripciones(self):
        return self.repositorioInscripcion.findAll()

    def actualizar(self, id, infoInscripcion, id_estudiante, id_materia):
        inscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcion.año = infoInscripcion['año']
        inscripcion.semestre = infoInscripcion['semestre']
        inscripcion.nota_final = infoInscripcion['nota_final']
        estudiante = Estudiante(self.repositorioEstudiante.findById(id_estudiante))
        materia = Materia(self.repositorioMateria.findById(id_materia))
        inscripcion.estudiante = estudiante
        inscripcion.materia = materia
        return self.RepositorioInscripcion.save(inscripcion)

    def eliminar(self,id):
        return self.repositorioInscripcion.delete(id)

    def listarInscritosEnMateria(self, id_materia):
        return self.repositorioInscripcion.getListadoInscripcionMateria(id_materia)

    def notaMayorporCurso(self):
        return self.repositorioInscripcion.getMayorNotaporCurso()

    def promedioNotasMateria(self,id_materia):
        return self.repositorioInscripcion.promedioNotasEnMateria(id_materia)
