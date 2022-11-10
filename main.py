from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorResultado import ControladorResultado
import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)
miControladorResultado = ControladorResultado()

#LINEA ADICIONAL
@app.route("/",methods=["GET"])
def test():
    json={}
    json ["mensaje"]= "Servidor ejecutandose"
    return jsonify(json)


#LINEA RESULTADOS
@app.route("/resultados",methods=["POST"])
def crearResultado():
    data = request.get_json()
    respuestaCrear = miControladorResultado.crear(data)
    return jsonify(respuestaCrear)

@app.route("/resultados/<string:id>", methods =["GET"])
def consultarResultado(id):
    respuestaConsultar = miControladorResultado.mostrarResultado(id)
    return jsonify(respuestaConsultar)

@app.route("/resultados",methods=["GET"])
def consultarResultados():
    respuestaConsultar = miControladorResultado.mostrarResultados()
    return jsonify(respuestaConsultar)

@app.route("/resultados/<string:id>", methods = ["PUT"])
def actualizarResultado(id):
    datos = request.get_json()
    respuestaActualizar = miControladorResultado.actualizar(id,datos)
    return jsonify(respuestaActualizar)

@app.route("/resultados/<string:id>", methods = ["DELETE"])
def eliminarResultado(id):
    respuestaEliminar = miControladorResultado.eliminar(id)
    return jsonify(respuestaEliminar)

#LINEA ADICIONAL
def loadFileConfig():
    with open("config.json") as f:
        data = json.load(f)
    return data

if __name__=="__main__":
    dataConfig = loadFileConfig()
    print("servidor corriendo en: "+dataConfig["url-backend"]+ " puerto: "+str(dataConfig["port"]))
    serve(app, host = dataConfig["url-backend"], port = dataConfig["port"])
