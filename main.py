from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorCandidato import ControladorCandidato
import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)
miCandidato = ControladorCandidato()


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


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Servidor corriendo en: " + dataConfig['url-backend'] + " puerto: " + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])
