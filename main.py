from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartidos import ControladorPartidos
import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Robinson:Cindy2022@cluster0.wixxz28.mongodb.net/bd-registro?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)
baseDatos = client["bd-registro"]
print(baseDatos.list_collection_names())

app = Flask(__name__)
cors = CORS(app)
miCandidato = ControladorCandidato()
miPartido = ControladorPartidos()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json['mensaje'] = "Servidor ejecutándose"
    return jsonify(json)


@app.route("/candidato", methods=['POST'])
def crearcandidatos():
    data = request.get_json()
    respuestacrear = miCandidato.crearcandidato(data)
    return jsonify(respuestacrear)


@app.route("/candidato/<string:id>", methods=['GET'])
def consultarCandidato(id):
    respuestaConsultar = miCandidato.mostrarcandidato(id)
    return jsonify(respuestaConsultar)


@app.route("/candidato", methods=['GET'])
def consultarCandidatos():
    respuestaConsultar = miCandidato.mostrarcandidatos()
    return jsonify(respuestaConsultar)


@app.route("/candidato/<string:id>", methods=['PUT'])
def actualizarCandidatos(id):
    datos = request.get_json()
    respuestaActualizar = miCandidato.actualizar(id, datos)
    return jsonify(respuestaActualizar)


@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidatos(id):
    respuestaEliminar = miCandidato.eliminar(id)
    return jsonify(respuestaEliminar)


@app.route("/partidos", methods=['POST'])
def crearPartidos():
    data = request.get_json()
    respuestacrear = miPartido.crearPartido(data)
    return jsonify(respuestacrear)


@app.route("/partidos/<string:id>", methods=['GET'])
def consultarPartido(id):
    respuestaConsultar = miPartido.mostrarPartido(id)
    return jsonify(respuestaConsultar)


@app.route("/partidos", methods=['GET'])
def consultarPartidos():
    respuestaConsultar = miPartido.mostrarPartidos()
    return jsonify(respuestaConsultar)


@app.route("/partidos/<string:id>", methods=['PUT'])
def actualizarPartidos(id):
    datos = request.get_json()
    respuestaActualizar = miPartido.actualizar(id, datos)
    return jsonify(respuestaActualizar)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartidos(id):
    respuestaEliminar = miPartido.eliminar(id)
    return jsonify(respuestaEliminar)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Servidor corriendo en: " + dataConfig['url-backend'] + " puerto: " + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])
