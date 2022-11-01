from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Departamento import Departamento
from Modelos.Materia import Materia

class Controladormateria():
    def __init__(self):
        print("Creando Controlador Materia")
        self.repositorioDepartamento = RepositorioDepartamento()
        self.repositorioMateria = RepositorioMateria()

    def crear(self, infoMateria):
        print("Crear una materia")
        materia = Materia(infoMateria)
        return self.repositorioMateria.save(materia)

    def mostrarMateria(self, id):
        print("Mostrando la materia con id: "+id)
        materia = Materia(self.repositorioMateria.findById(id))
        return materia.__dict__

    def mostrarMaterias(self):
        print("Mostrando todas las materias")
        return self.repositorioMateria.findAll()

    def actualizar(self,id,infoMateria):
        print("Actualizando la materia con id: "+id)
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def eliminar(self,id):
        print("eliminando la materia con id: "+id)
        return self.repositorioMateria.delete(id)

    #Relación entre materia y departamento
    def asignarDepartamento(self,id, id_departamento):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)