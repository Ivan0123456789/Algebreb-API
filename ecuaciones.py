from sympy import *
from sympy.abc import x
import sympy

from algebreb.listas.listas_ecuaciones_univariables import ListaEcuacionesGrado1, ListaEcuacionesGrado2

def lista_grado1(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    dominio = json['dominio']
    fraccion = json['fraccion']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['fraccion'] = fraccion
    caracteristicas['dominio'] = dominio
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaEcuacionesGrado1(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_grado2(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    dominio = json['dominio']
    fraccion = json['fraccion']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['fraccion'] = fraccion
    caracteristicas['dominio'] = dominio
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaEcuacionesGrado2(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc