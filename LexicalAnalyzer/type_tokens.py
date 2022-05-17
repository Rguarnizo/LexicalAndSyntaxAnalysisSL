#!/usr/bin/env python3
from .Symbols.math_symbols import *
from .Symbols.comparation_symbols import *
from .Symbols.reserve_words import *
from .Symbols.symbols import *
from .token import Token
from .type import type


def type_token(token,col,row):
  
  if(token in reservadas):
    return (Token(token,col,row),False)
  if(token in simbolos):
    return (Token(simbolos[token],col,row,tipo=token),False)
  if(token in math_simbolos):
    return (Token(math_simbolos[token],col,row,tipo=token),False)
  if(token in comparation_symbols):
    return (Token(comparation_symbols[token],col,row,token),False)
  if(token.startswith("'") or token.startswith('"')):
    return (Token(token,col,row,"tk_cadena"),False)
  if(token[0].isdigit()):
    return (Token(token,col,row,"tk_numero"),False)
  if(type(token[0],0)[0] in ['A-Z','_']):
    return (Token(token,col,row,"id"),False)
  return (Token('!',col,row,error=True),True)