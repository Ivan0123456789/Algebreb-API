from sympy import *
from sympy.abc import x
import sympy

from algebreb.listas.listas_fracciones_algebraicas import (ListaSumaFraccionesAlgebraicas, 
                                                           ListaRestaFraccionesAlgebraicas,
                                                           ListaMultFraccionesAlgebraicas,
                                                           ListaDivFraccionesAlgebraicas,
                                                           ListaSimpFraccionesAlgebraicas)
                                                           
def lista_suma_fracciones(json):
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

    lbc = ListaSumaFraccionesAlgebraicas(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_resta_fracciones(json):
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

    lbc = ListaRestaFraccionesAlgebraicas(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_mult_fracciones(json):
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

    lbc = ListaMultFraccionesAlgebraicas(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_div_fracciones(json):
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

    lbc = ListaDivFraccionesAlgebraicas(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc

def lista_simp_fracciones(json):
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

    lbc = ListaSimpFraccionesAlgebraicas(caracteristicas)
    lista_dicc = lbc.as_str_latex()

    return lista_dicc