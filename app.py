# <-- flask ..>
from flask import Flask, json, jsonify, request

# <-- algebreb -->

# <--sympy -->
from sympy import *
from sympy.abc import x

# <-- json -->
import json

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/binomios_cuadrados', methods=['GET'])
def binomios_cuadrados():
    title = request.json['title']

    print(request.json)
    return title

if __name__ == '__main__':
    app.run(debug=True, port=4000)