from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.Controladorestudiante import Controladorestudiante
from Controladores.Controladordepartamentoss import Controladordepartamento
from Controladores.Controladormateria import Controladormateria
from Controladores.Controladorinscripcion import Controladorinscripcion
import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)
miControladorEstudiante = Controladorestudiante()
miControladorDepartamento = Controladordepartamento()
miControladorMateria = Controladormateria()
miControladorInscripcion = Controladorinscripcion()

@app.route("/",methods=['GET'])
def test():
    json= {}
    json['mensaje']= "Servidor ejecutándose"
    return jsonify(json)

@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    respuestaCrear = miControladorEstudiante.crear(data)
    return jsonify(respuestaCrear)

@app.route("/estudiantes/<string:id>", methods=['GET'])
def consultarEstudiante(id):
    respuestaConsultar = miControladorEstudiante.mostrarEstudiante(id)
    return jsonify(respuestaConsultar)

@app.route("/estudiantes",methods=['GET'])
def consultarEstudiantes():
    respuestaConsultar = miControladorEstudiante.mostrarEstudiantes()
    return jsonify(respuestaConsultar)

@app.route("/estudiantes/<string:id>", methods = ['PUT'])
def actualizarEstudiante(id):
    datos = request.get_json()
    respuestaActualizar = miControladorEstudiante.actualizar(id,datos)
    return jsonify(respuestaActualizar)

@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    respuestaEliminar = miControladorEstudiante.eliminar(id)
    return jsonify(respuestaEliminar)

#SERVICIOS DEPARTAMENTOS

@app.route("/departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    respuestaCrear = miControladorDepartamento.crear(data)
    return jsonify(respuestaCrear)

@app.route("/departamentos/<string:id>", methods=['GET'])
def consultarDepartamento(id):
    respuestaConsultar = miControladorDepartamento.mostrarDepartamento(id)
    return jsonify(respuestaConsultar)

@app.route("/departamentos",methods=['GET'])
def consultarDepartamentos():
    respuestaConsultar = miControladorDepartamento.mostrarDepartamentos()
    return jsonify(respuestaConsultar)

@app.route("/departamentos/<string:id>", methods = ['PUT'])
def actualizarDepartamento(id):
    datos = request.get_json()
    respuestaActualizar = miControladorDepartamento.actualizar(id,datos)
    return jsonify(respuestaActualizar)

@app.route("/departamentos/<string:id>", methods=['DELETE'])
def eliminarDepartamento(id):
    respuestaEliminar = miControladorDepartamento.eliminar(id)
    return jsonify(respuestaEliminar)

#SERVICIOS MATERIAS

@app.route("/materias",methods=['POST'])
def crearMateria():
    data = request.get_json()
    respuestaCrear = miControladorMateria.crear(data)
    return jsonify(respuestaCrear)

@app.route("/materias/<string:id>", methods=['GET'])
def consultarMateria(id):
    respuestaConsultar = miControladorMateria.mostrarMateria(id)
    return jsonify(respuestaConsultar)

@app.route("/materias",methods=['GET'])
def consultarMaterias():
    respuestaConsultar = miControladorMateria.mostrarMaterias()
    return jsonify(respuestaConsultar)

@app.route("/materias/<string:id>", methods = ['PUT'])
def actualizarMateria(id):
    datos = request.get_json()
    respuestaActualizar = miControladorMateria.actualizar(id,datos)
    return jsonify(respuestaActualizar)

@app.route("/materias/<string:id>", methods=['DELETE'])
def eliminarMateria(id):
    respuestaEliminar = miControladorMateria.eliminar(id)
    return jsonify(respuestaEliminar)

@app.route("/materias/<string:id>/departamentos/<string:id_departamento>",methods=['PUT'])
def asignarDepartamentoMateria(id,id_departamento):
    respuestaAsignar = miControladorMateria.asignarDepartamento(id,id_departamento)
    return jsonify(respuestaAsignar)

@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    datos = request.get_json()
    respuestaCrear = miControladorInscripcion.crear(datos,id_estudiante,id_materia)
    return jsonify(respuestaCrear)

@app.route("/inscripciones/<string:id>", methods =['GET'])
def consultarInscripcion(id):
    respuestaConsultar = miControladorInscripcion.mostrarInscripcion(id)
    return jsonify(respuestaConsultar)

@app.route("/inscripciones", methods =['GET'])
def consultarInscripciones():
    respuestaConsultar = miControladorInscripcion.mostrarInscripciones()
    return jsonify(respuestaConsultar)

@app.route("/inscripciones/<string:id>/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods=['PUT'])
def actualizarInscripcion(id,id_estudiante,id_materia):
    datos = request.get_json()
    respuestaActualizar = miControladorInscripcion.actualizar(id,datos,id_estudiante,id_materia)
    return jsonify(respuestaActualizar)

@app.route("/inscripciones/<string:id>", methods = ['DELETE'])
def eliminarInscripcion(id):
    respuestaEliminar = miControladorInscripcion.eliminar(id)
    return jsonify(respuestaEliminar)

@app.route("/inscripciones/materia/<string:id_materia>", methods = ['GET'])
def inscritosMateria(id_materia):
    respuestaInscritos = miControladorInscripcion.listarInscritosEnMateria(id_materia)
    return jsonify(respuestaInscritos)

@app.route("/inscripciones/notaMayor", methods = ['GET'])
def notaMayorMateria():
    respuestaNota = miControladorInscripcion.notaMayorporCurso()
    return jsonify(respuestaNota)

@app.route("/inscripciones/promedio/materia/<string:id_materia>", methods = ['GET'])
def promedioNotas(id_materia):
    respuestaPromedio = miControladorInscripcion.promedioNotasMateria(id_materia)
    return jsonify(respuestaPromedio)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Servidor corriendo en: "+dataConfig['url-backend']+ " puerto: "+str(dataConfig['port']))
    serve(app, host = dataConfig['url-backend'], port=dataConfig['port'])