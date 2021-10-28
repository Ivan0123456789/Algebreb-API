# <-- flask ..>
from flask import Flask, json, jsonify, request
from flask_cors import CORS, cross_origin

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

from polinomios import (lista_suma_polinomios,
                        lista_resta_polinomios,
                        lista_mult_polinomios,
                        lista_div_polinomios,
                        lista_grado_polinomios,
                        lista_term_polinomios)

from productos_notables import (lista_binomios_al_cuadrado,
                                lista_binomios_al_cubo, 
                                lista_binomios_conjugados, 
                                lista_binomios_forma1, 
                                lista_binomios_forma2,
                                lista_trinomios_al_cuadrado)

from fracciones_algebraicas import (lista_suma_fracciones,
                                    lista_resta_fracciones,
                                    lista_mult_fracciones, 
                                    lista_div_fracciones,
                                    lista_simp_fracciones)

from ecuaciones import lista_grado1, lista_grado2

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# <-- Permitir cors para todos los origenes -->
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# <-- Endpoint de prueba -->

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

# <-- Endpoints PRODUCTOS NOTABLES -->

@app.route('/binomios_al_cuadrado', methods=['POST'])
def binomios_al_cuadrado():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_al_cuadrado(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/binomios_al_cubo', methods=['POST'])
def binomios_al_cubo():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_al_cubo(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/binomios_conjugados', methods=['POST'])
def binomios_conjugados():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_conjugados(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/binomios_forma1', methods=['POST'])
def binomios_forma1():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_forma1(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/binomios_forma2', methods=['POST'])
def binomios_forma2():
    print(request.json)

    caracteristicas = request.json
    lista = lista_binomios_forma2(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/trinomios_al_cuadrado', methods=['POST'])
def trinomios_al_cuadrado():
    print(request.json)

    caracteristicas = request.json
    lista = lista_trinomios_al_cuadrado(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

# <-- Endpoints FACTORIZACION -->

@app.route('/factor_comun', methods=['POST'])
def factor_comun():
    print(request.json)

    caracteristicas = request.json
    lista = lista_factor_comun(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/diferencia_cuadrados', methods=['POST'])
def diferencia_cuadrados():
    print(request.json)

    caracteristicas = request.json
    lista = lista_diferencia_cuadrados(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/trinomio_cuadrado_perfecto', methods=['POST'])
def trinomio_cuadrado_perfecto():
    print(request.json)

    caracteristicas = request.json
    lista = lista_trinomio_cuadrado_perfecto(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/cubo_perfecto_binomios', methods=['POST'])
def cubo_perfecto_binomios():
    print(request.json)

    caracteristicas = request.json
    lista = lista_cubo_perfecto_binomios(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/trinomio_forma1', methods=['POST'])
def trinomio_forma1():
    print(request.json)

    caracteristicas = request.json
    lista = lista_trinomios_forma1(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/trinomio_forma2', methods=['POST'])
def trinomio_forma2():
    print(request.json)

    caracteristicas = request.json
    lista = lista_trinomios_forma2(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

# <-- Endpoints FRACCIONES ALGEBRAICAS -->

@app.route('/suma_fracciones', methods=['POST'])
def suma_fracciones():
    print(request.json)

    caracteristicas = request.json
    lista = lista_suma_fracciones(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/resta_fracciones', methods=['POST'])
def resta_fracciones():
    print(request.json)

    caracteristicas = request.json
    lista = lista_resta_fracciones(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/multiplicacion_fracciones', methods=['POST'])
def multiplicacion_fracciones():
    print(request.json)

    caracteristicas = request.json
    lista = lista_mult_fracciones(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/division_fracciones', methods=['POST'])
def division_fracciones():
    print(request.json)

    caracteristicas = request.json
    lista = lista_div_fracciones(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/simplificacion_fracciones', methods=['POST'])
def simplificacion_fracciones():
    print(request.json)

    caracteristicas = request.json
    lista = lista_simp_fracciones(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

# <-- Endpoints POLINOMIOS -->

@app.route('/suma_polinomios', methods=['POST'])
def suma_polinomios():
    print(request.json)

    caracteristicas = request.json
    lista = lista_suma_polinomios(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/resta_polinomios', methods=['POST'])
def resta_polinomios():
    print(request.json)

    caracteristicas = request.json
    lista = lista_resta_polinomios(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta
    
@app.route('/multiplicacion_polinomios', methods=['POST'])
def multiplicacion_polinomios():
    print(request.json)

    caracteristicas = request.json
    lista = lista_mult_polinomios(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/division_polinomios', methods=['POST'])
def division_polinomios():
    print(request.json)

    caracteristicas = request.json
    lista = lista_div_polinomios(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/grado_polinomios', methods=['POST'])
def grado_polinomios():
    print(request.json)

    caracteristicas = request.json
    lista = lista_grado_polinomios(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

@app.route('/termino_polinomios', methods=['POST'])
def termino_polinomios():
    print(request.json)

    caracteristicas = request.json
    lista = lista_term_polinomios(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

# <-- Endpoints ECUACIONES -->
@app.route('/ecuaciones_grado1', methods=['POST'])
def ecuaciones_grado1():
    print(request.json)

    caracteristicas = request.json
    lista = lista_grado1(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta

# <-- Endpoints ECUACIONES -->
@app.route('/ecuaciones_grado2', methods=['POST'])
def ecuaciones_grado2():
    print(request.json)

    caracteristicas = request.json
    lista = lista_grado2(caracteristicas)
    json_object = json.dumps(lista, indent=4)
    respuesta = jsonify(json_object)

    return respuesta


if __name__ == '__main__':
    app.run(debug=True, port=4000)