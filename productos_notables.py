from sympy import *
from sympy.abc import x
import sympy

from algebreb.listas.listas_productos_notables import (ListaBinomioAlCuadrado, 
                                                       ListaBinomioAlCubo, 
                                                       ListaBinomiosConjugados, 
                                                       ListaBinomiosFormaI, 
                                                       ListaBinomiosFormaII, 
                                                       ListaTrinomioAlCuadrado)

def lista_binomios_al_cuadrado(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    dom = json['dominio']
    fracc = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['dominio'] = dom
    caracteristicas['fraccion'] = fracc
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaBinomioAlCuadrado(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_binomios_al_cubo(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    dom = json['dominio']
    fracc = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['dominio'] = dom
    caracteristicas['fraccion'] = fracc
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaBinomioAlCubo(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_binomios_conjugados(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    dom = json['dominio']
    fracc = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['dominio'] = dom
    caracteristicas['fraccion'] = fracc
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaBinomiosConjugados(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_binomios_forma1(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaBinomiosFormaI(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_binomios_forma2(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaBinomiosFormaII(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_trinomios_al_cuadrado(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    dom = json['dominio']
    fracc = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['dominio'] = dom
    caracteristicas['fraccion'] = fracc
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaTrinomioAlCuadrado(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc