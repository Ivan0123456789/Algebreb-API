from sympy import *
from sympy.abc import x
import sympy

from algebreb.listas.listas_polinomios import (ListaSumaPolinomios,
                                               ListaRestaPolinomios,
                                               ListaMultPolinomios,
                                               ListaDivPolinomios,
                                               ListaTermPolinomio,
                                               ListaGradoPolinomios)

def lista_suma_polinomios(json):
    cant = json['cantidad']
    variables = json['variables']
    completo = json['completo']
    dominio = json['dominio']
    fraccion = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['completo'] = completo
    caracteristicas['dominio'] = dominio
    caracteristicas['fraccion'] = fraccion
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaSumaPolinomios(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_resta_polinomios(json):
    cant = json['cantidad']
    variables = json['variables']
    completo = json['completo']
    dominio = json['dominio']
    fraccion = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['completo'] = completo
    caracteristicas['dominio'] = dominio
    caracteristicas['fraccion'] = fraccion
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaRestaPolinomios(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_mult_polinomios(json):
    cant = json['cantidad']
    variables = json['variables']
    completo = json['completo']
    dominio = json['dominio']
    fraccion = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['completo'] = completo
    caracteristicas['dominio'] = dominio
    caracteristicas['fraccion'] = fraccion
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaMultPolinomios(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_div_polinomios(json):
    cant = json['cantidad']
    variables = json['variables']
    completo = json['completo']
    dominio = json['dominio']
    fraccion = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']
    exacta = json['exacta']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['completo'] = completo
    caracteristicas['dominio'] = dominio
    caracteristicas['fraccion'] = fraccion
    caracteristicas['exacta'] = exacta
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaDivPolinomios(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_grado_polinomios(json):
    cant = json['cantidad']
    variables = json['variables']
    completo = json['completo']
    dominio = json['dominio']
    fraccion = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['completo'] = completo
    caracteristicas['dominio'] = dominio
    caracteristicas['fraccion'] = fraccion
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaGradoPolinomios(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_term_polinomios(json):
    cant = json['cantidad']
    variables = json['variables']
    completo = json['completo']
    dominio = json['dominio']
    fraccion = json['fraccion']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['completo'] = completo
    caracteristicas['dominio'] = dominio
    caracteristicas['fraccion'] = fraccion
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaTermPolinomio(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc