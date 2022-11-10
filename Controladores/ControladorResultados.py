from Modelos.Resultado import Resultado
class ControladorResultado():
    def __init__(self):
        print("Creando Controlador Resultado")

    def crear(self, infoResultado):
        print("Crear un Resultado")
        resultado = Resultado(infoResultado)
        return resultado.__dict__

    def mostrarResultado(self, id):
        print("Mostrando el resultado con id: "+id)
        resultado={
            "_id":id,
            "numero_mesa":"12",
            "id_candidato":"3",

        }
        return resultado

    def mostrarResultados(self):
        print("Mostrando todos los resultados")
        unResultado = {
            "_id":"123",
            "numero_mesa":"12",
            "id_candidato":"3",

        }
        return [unResultado]

    def actualizar(self,id,infoResultado):
        print("Actualizando el resultado con id: "+id)
        resultado = Resultado(infoResultado)
        return resultado.__dict__

    def eliminar(self,id):
        print("eliminando el resultado con id: "+id)
        return {"deleted_count":1}