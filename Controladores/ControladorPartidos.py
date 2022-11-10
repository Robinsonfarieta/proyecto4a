from Modelos.Partidos import Partidos
from Repositorios.RepositorioPartidos import RepositorioPartidos

class ControladorPartidos():
    def __init__(self):
        print("Creando controlador de partidos")
        self.repositorioPartidos = RepositorioPartidos()

    def crearPartido(self, infoPartido):
        print("Crear un Partido")
        partidos = Partidos(infoPartido)
        return self.repositorioPartidos.save(partidos)

    def mostrarPartido(self, id):
        print("Mostrando el partido con id: "+ id)
        partidos = Partidos(self.repositorioPartidos.findById(id))
        return partidos.__dict__

    def mostrarPartidos(self):
        print("Mostrando todos los partidos")
        return self.repositorioPartidos.findAll()

    def actualizar(self,id,infoPartidos):
        print("Actualizando el partido con id: "+id)
        partidoActual = Partidos(self.repositorioPartidos.findById(id))
        partidoActual.nombre = infoPartidos["nombre"]
        partidoActual.lema = infoPartidos["lema"]
        return self.repositorioPartidos.save(partidoActual)

    def eliminar(self,id):
        print("Eliminando el partido con id: "+id)
        return self.repositorioPartidos.delete(id)