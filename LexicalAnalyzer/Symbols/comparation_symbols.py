#!/usr/bin/env python3


comparation_symbols1 = {
    '<': 'tk_menor',
    '<=': 'tk_menor_igual',
    '<>': 'tk_distinto_de',
    '==': 'tk_igual_que',
    '>': 'tk_mayor',
    '>=': 'tk_mayor_igual',
}


comparation_symbols2 ={
    '=': 'tk_asignacion',
}

comparation_symbols = {**comparation_symbols1, **comparation_symbols2}
