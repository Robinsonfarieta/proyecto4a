from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Departamento import Departamento


class Controladordepartamento():
    def __init__(self):
        print("Creando Controlador Departamento")
        self.repositorioDepartamento = RepositorioDepartamento()

    def crear(self, infoDepartamento):
        print("Crear un departamento")
        departamento = Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(departamento)

    def mostrarDepartamento(self, id):
        print("Mostrando el departamento con id: "+id)
        departamento = Departamento(self.repositorioDepartamento.findById(id))
        return departamento.__dict__

    def mostrarDepartamentos(self):
        print("Mostrando todos los departamentos")
        return self.repositorioDepartamento.findAll()

    def actualizar(self,id,infoDepartamento):
        print("Actualizando el departamento con id: "+id)
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id))
        departamentoActual.nombre = infoDepartamento["nombre"]
        return self.repositorioDepartamento.save(departamentoActual)

    def eliminar(self,id):
        print("eliminando el departamento con id: "+id)
        return self.repositorioDepartamento.delete(id)