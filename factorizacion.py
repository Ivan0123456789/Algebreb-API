from sympy import *
from sympy.abc import x
import sympy

from algebreb.listas.listas_factorizacion import (ListaFactorComun,
                                                  ListaDiferenciaCuadrados,
                                                  ListaCuboPerfectoBinomios,
                                                  ListaTrinomioCuadradoPerfecto,
                                                  ListaTrinomioFormaI,
                                                  ListaTrinomioFormaII)

def lista_factor_comun(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    completo = json['completo']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['completo'] = completo
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaFactorComun(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_diferencia_cuadrados(json):
    caracteristicas = {}

    cant = json['cantidad']
    variables = json['variables']
    gmin = json['gmin']
    gmax = json['gmax']
    cmin = json['cmin']
    cmax = json['cmax']

    vars_as_symbols = [sympy.symbols(v) for v in variables]

    caracteristicas = {}
    caracteristicas['cantidad'] = cant
    caracteristicas['variables'] = vars_as_symbols
    caracteristicas['gmin'] = gmin
    caracteristicas['gmax'] = gmax
    caracteristicas['cmin'] = cmin
    caracteristicas['cmax'] = cmax

    lbc = ListaDiferenciaCuadrados(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_trinomio_cuadrado_perfecto(json):
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

    lbc = ListaTrinomioCuadradoPerfecto(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_cubo_perfecto_binomios(json):
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

    lbc = ListaCuboPerfectoBinomios(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_trinomios_forma1(json):
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

    lbc = ListaTrinomioFormaI(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_trinomios_forma2(json):
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

    lbc = ListaTrinomioFormaII(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc