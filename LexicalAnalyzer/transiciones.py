#!/usr/bin/env python3
from .Symbols.math_symbols import *
from .Symbols.comparation_symbols import *
from .Symbols.reserve_words import *
from .Symbols.symbols import *

transiciones = {
    #Symbols
    (0,'other'):(0,0),
    (0,'symbol'):(0,0),
    (0,'tk_multiplicacion'):(0,0),
    (0,'tk_resta'):(0,0),
    (0,'tk_suma'):(0,0),


    #Numeros
    (0,'0-9'):(1,0),

    (1,'0-9'):(1,0),
    (1,'tk_punto'):(2,0),
    (1,'e'):(4,0),
    (1,'E'):(4,0),
    (1,'A-Z'):(0,1),
    (1,'other'):(0,1),
    (1,'symbol'):(0,1),


    (2,'0-9'):(3,0),
    (2,'tk_punto'):(0,2),
    (2,'A-Z'):(0,2),
    (2,'other'):(0,2),
    (2,'symbol'):(0,2),


    (3,'0-9'):(3,0),
    (3,'E'):(4,0),
    (3,'e'):(4,0),
    (3,'other'):(0,1),
    (3,'A-Z'):(0,1),
    (3,'symbol'):(0,1),

    (4,'tk_resta'):(5,0),
    (4,'tk_suma'):(5,0),
    (4,'other'):(0,2),
    (4,'symbol'):(0,1),
    (4,'A-Z'):(0,2),
    (4,'0-9'):(6,0),

    (5,'0-9'): (6,0),
    (5,'other'):(0,3),
    (5,'A-Z'):(0,3),
    (5,'symbol'):(0,1),

    (6,'0-9'):(6,0),
    (6,'A-Z'):(0,1),
    (6,'other'):(0,1),

    #Palabras Reservadas o Id's
    (0,'A-Z'):(7,0),
    (0,'e'):(7,0),

    (7,'A-Z'):(7,0),
    (7,'0-9'):(7,0),
    (7,'symbol'):(0,1),
    (7,'other'):(0,1),

    #Comentarios
    (0,'tk_division'):(8,0),

    (8,'tk_division'):(9,0),
    (8,'tk_multiplicacion'):(10,0),
    (8,'other'):(0,1),
    (8,'A-Z'):(0,1),
    (8,'0-9'):(0,1),

    (9,'A-Z'):(9,0),
    (9,'0-9'):(9,0),
    (9,'other'):(9,0),
    (9,'"'):(9,0),
    (9,'symbol'):(9,0),
    (9,'\n'):(0,0),

    (10,'A-Z'):(10,0),
    (10,'0-9'):(10,0),
    (10,'other'):(10,0),
    (10,'symbol'): (10,0),
    (10,'tk_multiplicacion'):(11,0),
    (10,'"'):(10,0),
    (10,"'"):(10,0),
    (10,"tk_punto"):(10,0),
    (10, 'tk_resta'): (10, 0),
    (10, 'tk_suma'): (10, 0),
    (10,"tk_division"): (10,0),
    (10, 'tk_asignacion'):(10,0),

    (11,'A-Z'):(10,0),
    (11,'0-9'):(10,0),
    (11,'other'):(10,0),
    (11,'tk_multiplicacion'):(11,0),
    (11,'tk_division'):(0,0),

    #Simbolos
    (0,'tk_menor'):(12,0),
    (12,'tk_mayor'):(0,0),
    (12,'A-Z'):(0,1),
    (12,'0-9'):(0,1),
    (12,'other'):(0,1),
    (12,'symbol'):(0,1),
    (12,'tk_asignacion'):(0,0),
    (12,'other'):(0,1),

    (0,'tk_asignacion'):(13,0),
    (13,'tk_asignacion'):(0,0),
    (13,'A-Z'):(0,1),
    (13,'0-9'):(0,1),
    (13,'other'):(0,1),
    (13,'symbol'):(0,1),
    (13,'other'):(0,1),

    (0,'tk_mayor'):(14,0),
    (14,'tk_asignacion'):(0,0),
    (14,'A-Z'):(0,1),
    (14,'0-9'):(0,1),
    (14,'other'):(0,1),
    (14,'symbol'):(0,1),
    (14,'other'):(0,1),

    (0,'tk_punto'):(0,0),

    #Cadenas
    (0,'"'):(20,0),
    (20,'A-Z'):(20,0),
    (20,'0-9'):(20,0),
    (20,'other'):(20,0),
    (20,'symbol'):(20,0),
    (20,'"'):(0,0),

    (0,"'"):(22,0),
    (22,'A-Z'):(22,0),
    (22,'0-9'):(22,0),
    (22,'other'):(22,0),
    (22,'symbol'):(22,0),
    (22,'"'):(22,0),
    (22,"'"):(0,0),
}


math = {(i,y):(0,1) for i in [1,3,5,6,12,13,14] for x,y in math_simbolos.items() if x != '.'}
comparation = {(i,y):(0,1) for i in [1,3,5,6] for x,y in comparation_symbols.items()}

another_one = { (0,y):(0,0) for x,y in math_simbolos.items() if x != '/'}
another_two = { (9,y):(9,0) for x,y in math_simbolos.items() if x != '/'}
another_three = { (10,y):(10,0) for x,y in math_simbolos.items() if x != '*'}

another = {(7,y):(7,0) for x,y in math_simbolos.items()}
symbols = {(0,y):(0,0) for x,y in simbolos.items()}


transiciones.update(math)
transiciones.update(comparation)
transiciones.update(symbols)
transiciones.update(another)
transiciones.update(another_one)
transiciones.update(another_two)
transiciones.update(another_three)
