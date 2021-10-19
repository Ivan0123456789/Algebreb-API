# <-- flask ..>
from flask import Flask, json, jsonify, request

# <--sympy -->
from sympy import *
from sympy.abc import x

# <-- json -->
import json

from productos_notables import (lista_binomios_al_cuadrado,
                                lista_binomios_al_cubo, 
                                lista_binomios_conjugados, 
                                lista_binomios_forma1, 
                                lista_binomios_forma2,
                                lista_trinomios_al_cuadrado)

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/binomios_al_cuadrado', methods=['GET'])
def binomios_al_cuadrado():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_al_cuadrado(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/binomios_al_cubo', methods=['GET'])
def binomios_al_cubo():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_al_cubo(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/binomios_conjugados', methods=['GET'])
def binomios_conjugados():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_conjugados(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/binomios_forma1', methods=['GET'])
def binomios_forma1():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_forma1(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/binomios_forma2', methods=['GET'])
def binomios_forma2():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_forma2(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/trinomios_al_cuadrado', methods=['GET'])
def trinomios_al_cuadrado():
    print(request.json)

    caracteristicas = request.json
    lista = lista_trinomios_al_cuadrado(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

if __name__ == '__main__':
    app.run(debug=True, port=4000)