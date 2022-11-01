from Repositorios.Interfaces import Interfaces
from Modelos.Inscripcion import Inscripcion
from bson import ObjectId

class RepositorioInscripcion(Interfaces[Inscripcion]):
    def getListadoInscripcionMateria(self, id_materia):
        consulta = {"materia.$id":ObjectId(id_materia)}
        return self.query(consulta)

    def getMayorNotaporCurso(self):
        query1={
            "$group":
                {
                    "_id":"$materia",
                    "max":{
                        "$max":"$nota_final"
                    },
                    "doc":{
                        "$first":"$$ROOT"
                    }
                }
        }
        pipeline=[query1]
        return self.queryAggregation(pipeline)

    def promedioNotasEnMateria(self, id_materia):
        query1 ={
            "$match":{"materia.$id":ObjectId(id_materia)}
        }
        query2 = {
            "$group":{
                "_id": "$materia",
                "promedio":{
                    "$avg":"$nota_final"
                }
            }
        }
        pipeline= [query1,query2]
        return self.queryAggregation(pipeline)

