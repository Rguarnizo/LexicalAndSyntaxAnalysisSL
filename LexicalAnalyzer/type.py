#!/usr/bin/env python3
from .Symbols.math_symbols import *
from .Symbols.comparation_symbols import *
from .Symbols.reserve_words import *
from .Symbols.symbols import *


def type(x,state):
  if(x >= '0' and x <= '9'):
    return ('0-9',x)

  if((x == '"') or (x == "'") and (state not in [9])):
    if(state == 20 and x == "'"):
      return ('other','other')
    if(state == 22 and x == '"'):
      return ('other','other')
    return (x,x)

  if(((x == 'e') or (x == 'E')) and (state in [1,3])):
    return (x,'A-Z')

  if((x >= 'A' and x <= 'Z') or (x >= 'a' and x <= 'z') or x is'_'):
    return ('A-Z',x)

  if((x in simbolos) and (state not in [9])):
    return ("symbol",x)

  if((x in math_simbolos) and (state not in [20,22,9,7])):
    return (math_simbolos[x],x)

  if((x in comparation_symbols) and (state not in [20,22,9,7])):
    return(comparation_symbols[x],x)

  return ('other','other')
