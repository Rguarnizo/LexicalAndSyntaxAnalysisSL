#!/usr/bin/env python3
from .Symbols.reserve_words import *
from .Symbols.comparation_symbols import *

class Token():

    def __init__(self,valor,col,row,tipo=0,error=False):
        self.col = col
        self.row = row
        self.valor = valor
        self.tipo = valor if tipo == 0 else tipo
        if(self.tipo in ['TRUE','FALSE','no']):
          self.tipo = 'tk_logico'
        if(self.tipo in reservadas2):
          self.tipo = 'id'
        if(self.tipo in comparation_symbols1):
          self.tipo = 'tk_comparation'
        self.error = error



    def __str__(self):
      if self.error:
        err = f'>>> Error lexico(linea:{self.col},posicion:{self.row})'
        return err
      return f'<{self.tipo},{self.valor},{self.col},{self.row}>'if self.tipo else f'<{self.valor},{self.col},{self.row}>'
