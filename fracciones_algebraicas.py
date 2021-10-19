from sympy import *
from sympy.abc import x
import sympy

from algebreb.listas.listas_fracciones_algebraicas import (ListaSumaFraccionesAlgebraicas)
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