Gramatica = {
    #? Producción Inicial | Nombre del programa.
"GRAM" : (["programa","id","A"],["A"]),

      #? Estructura  Constantes Tipos Variables Programa Subrutinas
      "A" : (["const","C","A"],["tipos","T","A"],["var","V","A"],["P","S"]),
        "C" : (["CONST"]),
        "T" : (["TYPE"]),
        "V" : (["VAR"]),
        "P" : (["inicio","PROGRAM","fin"]), 
        "S" : (["subrutina","SUB"]   ,['""']),

          #? Constatantes
          "CONST" : (["id","=","TCONST","OPTCOMMA","CONST"],['""']),
          "OPTCOMMA": ([";"],['""']),
          "TCONST": (["tk_cadena"],["tk_numero"],["tk_logico"]),
          #? Considerar inicialización de matrices (?)

          #? Tipos
          "TYPE"  : (["id",":","TTYPE","TYPE"],['""']),
          "TTYPE" : (["numerico"],["cadena"],["logico"],["REG"],["VEC"],["MATX"]),
         

          #? Variables
        
         "VAR": (["id","OTHERSVARS"],['""']),
        "OTHERSVARS":([",","id","OTHERSVARS"],["VARTYPE"]),
         "VARTYPE" : ([":","TVAR","COMMAOPYC","VAR"]),
         "COMMAOPYC": ([";"],[","],['""']),
         "TVAR" : (["numerico"],["id"],["cadena"],["logico"],["REG"],["VEC"],["MATX"]),

          #?  Vectores 
          "VEC"   : (["vector","[","SVEC","]","TVEC"]),
          "SVEC"  : (['*'],["tk_numero"],["id"]),
          "TVEC"  : (["numerico"],["cadena"],["logico"],["id"],["REG"]),

          #? Matrices
          "MATX"   : (["matriz","[","MATXARGS","]","TMATX"]),
          "MATXARGS"  : (["TMATXARG",",","TMATXARG","TMATX3"]),
          "TMATXARG"  : (['*'],["tk_numero"],["id"]),
          "TMATX3" : ([",","TMATXARG"],['""']),
          "TMATX"  : (["numerico"],["cadena"],["logico"],["id"],["REG"]),

          #? Registros
          "REG"   : (["registro","{","NREG","}"]),
          "NREG"  : (["VAR"],["{","NREG","}"]),
          
        #? Estructura de los programas   Expresiones  Sentencias  Funciones 
        "PROGRAM" : (["STCE","PROGRAM"],['""']),

        "STCE"  : (["si","COND"],["desde","DESDE"],["mientras","WHILE"],["repetir","DOWHILE"],["eval","EVAL"],["id","TIPOSCTE"],["RETORNA"]),
      "TIPOSCTE": (["ASIG"],["FUNC","OPCOMMA"]),

          "ASIG": (["INDEX","POINT","=","E","OPCOMMA"]),

          #TODO: Algo pasa con OPCOMA, A VECES NO FUNCIONA BIEN.
          "FUNC": (["(","ARGSFUNC",")"]),
       "OPCOMMA": ([";"],['""']),
      "ARGSFUNC": (["E","MARGSFUNC"],['""']),
    "MARGSFUNC" : ([",","E","MARGSFUNC"],['""']),

       "ACCESS":(["INDEX"],["POINT"]),

       "INDEX":(["[","E","MINDEX","]"],['""']),
       "MINDEX":([",","E","MINDEX"],['""']),

      "POINT":([".","id","MPOINTS"],['""']),
      "MPOINTS":([".","id","MPOINTS"],['""'],["INDEX"]),

          #? Expresiones Numericas
               "E": (["TIPOT","EV"],["(","E",")","EV"],["ECHANGE","E"],["{","EXPARR","}"]),
        "ECHANGE" :(["-"],["not"]),
              "EV": (["OP","E"],[';'],['""']),
           "TIPOT": (['id',"TIPOID"],['tk_numero'],['tk_cadena'],['tk_logico']),
           "TIPOID":(["ACCESS"],["FUNC"],['""']),
             "OP" : (["*"],["/"],["+"],["-"],["%"],["^"],["tk_comparation"],["and"],["or"]),

          #? Expresiones Array
            "EXPARR": (["MULTROWS"],["ACONST","MULTROWS"]),
          "MULTROWS": (["MATXARR","OTCOMMA","MULTROWS"],['""']),
          "OTCOMMA" : ([","],['""']),
            "MATXARR"  : (["{","ACONST","}"]),
            "ACONST": (["TARR","MACONST"],['""']),
           "MACONST": ([",","ACONST"],['""']),
            "TARR"  : (["tk_cadena"],["tk_numero"]),


            #?Condicionales Ciclos Evalución.
          
            #? For loop 
            "DESDE" : (["DES","hasta","M","PASO","{","PROGRAM","}"],['""']),
            "DES" : (["id","MANAGEDES"]),
       "MANAGEDES": (["=","TIPOM"]),
            "M" : (["id","MANAGEIDM"],["tk_numero"]),
          "MANAGEIDM": (["(","ARGSFUNC",")"],["OP","TIPOM"],['""']),
          "TIPOM":(["tk_numero"],["id"]),

            "PASO"  : (["paso","E"],['""']),


            "COND": (["(","E",")","{","SINOSI","PROGRAMSI","}"]),
            "SINOSI": (["sino","SI"],['""']),
            "SI": (["PROGRAMSI"],["si","E","PROGRAMSI"]),
            "PROGRAMSI" : (["STCESI","PROGRAMSI"],['""']),
            "STCESI" : (["id","TIPOSCTE"],["SINOSI"]),

             "LOOPS": (["WHILE"],["DOWHILE"],['""']),
             "WHILE": (["(","E",")","{","PROGRAM","}"]),
           "DOWHILE": (["PROGRAM","hasta","(","E",")"]),

            "EVAL"  : (["{","MEVAL","sino","PROGRAM","}"]),
            "MEVAL" : (["caso","(","E",")","PROGRAM","MEVAL"],['""']),

            "RETORNA": (["retorna","(","E",")"]),


        #? Subrutinas.
        "SUB"     : (["id","(","SUBARG",")","RET","A"],['""']),
        "RET"     : (["retorna","TSUBARG"],['""']),
       "SUBRUTINE": (["inicio","PROGRAM","fin"]),


       # TODO: Reformar por caso 42, Acepta subrutina(a, b, otro: numerico;)
        "SUBARG"  : (["SUBMID",":","TSUBARG","MSUBARG"],["ref","SUBMID",":","TSUBARG","MSUBARG"],['""']),
        "SUBMID"     : (["id","OTHERID"]),
        "OTHERID" : ([",","id","OTHERID"],['""']),
        "MSUBARG" : ([";","SUBARG"],['""']),
        "TSUBARG" : (["numerico"],["cadena"],["logico"],["id"],["VEC"],["MATX"]),

}