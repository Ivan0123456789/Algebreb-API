# <-- flask ..>
from flask import Flask, json, jsonify, request

# <--sympy -->
from sympy import *
from sympy.abc import x

# <-- json -->
import json

# <-- API -->
from factorizacion import (lista_cubo_perfecto_binomios, 
                           lista_diferencia_cuadrados, 
                           lista_factor_comun, 
                           lista_trinomio_cuadrado_perfecto, 
                           lista_trinomios_forma1, 
                           lista_trinomios_forma2)

from productos_notables import (lista_binomios_al_cuadrado,
                                lista_binomios_al_cubo, 
                                lista_binomios_conjugados, 
                                lista_binomios_forma1, 
                                lista_binomios_forma2,
                                lista_trinomios_al_cuadrado)

from fracciones_algebraicas import (lista_suma_fracciones)

app = Flask(__name__)

# <-- Endpoint de prueba -->

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

# <-- Endpoints PRODUCTOS NOTABLES -->

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

# <-- Endpoints FACTORIZACION -->

@app.route('/factor_comun', methods=['GET'])
def factor_comun():
    print(request.json)

    caracteristicas = request.json
    lista = lista_factor_comun(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/diferencia_cuadrados', methods=['GET'])
def diferencia_cuadrados():
    print(request.json)

    caracteristicas = request.json
    lista = lista_diferencia_cuadrados(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/trinomio_cuadrado_perfecto', methods=['GET'])
def trinomio_cuadrado_perfecto():
    print(request.json)

    caracteristicas = request.json
    lista = lista_trinomio_cuadrado_perfecto(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/cubo_perfecto_binomios', methods=['GET'])
def cubo_perfecto_binomios():
    print(request.json)

    caracteristicas = request.json
    lista = lista_cubo_perfecto_binomios(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/trinomio_forma1', methods=['GET'])
def trinomio_forma1():
    print(request.json)

    caracteristicas = request.json
    lista = lista_trinomios_forma1(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/trinomio_forma2', methods=['GET'])
def trinomio_forma2():
    print(request.json)

    caracteristicas = request.json
    lista = lista_trinomios_forma2(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/suma_fracciones', methods=['GET'])
def suma_fracciones():
    print(request.json)

    caracteristicas = request.json
    lista = lista_suma_fracciones(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta


if __name__ == '__main__':
    app.run(debug=True, port=4000)