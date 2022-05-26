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


grammarAngel = """Programa->ProgramaFirma BloqueDeclaraciones inicio BloqueSentencias ListaSentencias fin SubrutinasLista
ProgramaFirma->programa id
ProgramaFirma->ε
ListaDeclaraciones->Declaraciones ListaDeclaraciones
ListaDeclaraciones->ε
BloqueDeclaraciones->Declaraciones ListaDeclaraciones
BloqueDeclaraciones->ε
Declaraciones->const AsignacionConst FinSentencia ListaConst
ListaConst->AsignacionConst FinSentencia ListaConst
ListaConst->ε
Declaraciones->tipos id MasTiposVar : TipoDato FinSentencia ListaVarTipo
ListaVarTipo->id MasTiposVar : TipoDato FinSentencia ListaVarTipo
ListaVarTipo->ε
Declaraciones->var id MasTiposVar : TipoDato FinSentencia ListaVarTipo
TipoDato->TipoBasico
TipoDato->TipoComplejo
TipoBasico->numerico
TipoBasico->cadena
TipoBasico->logico
TipoBasico->id
TipoComplejo->vector [ VectorTamanio ] TipoBasico
TipoComplejo->matriz [ MatrizTamanio ] TipoBasico
TipoComplejo->registro { ListaVarTipo }
VectorTamanio->VectorValor
MatrizTamanio->VectorValor MatrizTamanioLista
MatrizTamanioLista->, MatrizTamanio
MatrizTamanioLista->ε
VectorValor->*
VectorValor->Expresion
ListaArgumentos->, Argumento ListaArgumentos
ListaArgumentos->ε
CuerpoSi->ListaSentencias SinoSentenciaLista
SinoSiSentencia->ListaSentencias
ListaSentencias->BloqueSentencias ListaSentencias
ListaSentencias->ε
BloqueSentencias->Sentencia FinSentencia
FinSentencia->ε
FinSentencia->;
Sentencia->SentenciaAsignFunc
Sentencia->SentenciaMientras
Sentencia->SentenciaRepetirHasta
Sentencia->SentenciaEval
Sentencia->SentenciaDesde
Sentencia->SentenciaRetorna
Sentencia->SentenciaSi
SentenciaSi->si ( Expresion ) { CuerpoSi }
SinoSentenciaLista->ε
SinoSentenciaLista->SinoSentencia SinoSentenciaLista
SinoSentencia->sino SinoSiSentencia
SinoSiSentencia->si ( Expresion ) ListaSentencias
SentenciaMientras->mientras ( Expresion ) { ListaSentencias }
SentenciaRepetirHasta->repetir ListaSentencias hasta ( Expresion )
SentenciaEval->eval { EvalCuerpo ListaCasosEval SinoEval }
ListaCasosEval->EvalCuerpo ListaCasosEval
ListaCasosEval->ε
EvalCuerpo->caso ( Expresion ) ListaSentencias
SinoEval->sino ListaSentencias
SinoEval->ε
SentenciaDesde->desde SentenciaAsignFunc hasta Expresion OpcionalPaso { ListaSentencias }
OpcionalPaso->paso Expresion
OpcionalPaso->ε
SentenciaRetorna->retorna ( Expresion )
AsignacionConst->Id = Expresion
SentenciaAsignFunc->Id SentenciaId
SentenciaId->= Expresion
SentenciaId->( Argumento ListaArgumentos )
Argumento->Expresion
Argumento->ε
Elemento->Expresion
Expresion->NegacionOpcional ExpresionTerminal ExpresionOperador
ExpresionOperador->Operador ExpresionFin
ExpresionFin->NegacionOpcional ExpresionTerminal ExpresionOperador
ExpresionOperador->ε
ExpresionTerminal->( Expresion )
ExpresionTerminal->Signo NumIdTerminal
NumIdTerminal->num
NumIdTerminal->Id FuncionId
FuncionId->ε
FuncionId->( Argumento ListaArgumentos )
Signo->ε
Signo->+
Signo->-
ExpresionTerminal->cadena_
NegacionOpcional->not
NegacionOpcional->ε
ExpresionTerminal->TRUE
ExpresionTerminal->FALSE
ExpresionTerminal->SI
ExpresionTerminal->NO
ExpresionTerminal->Objeto
Operador->+
Operador->-
Operador->*
Operador->/
Operador->%
Operador->^
Operador->and
Operador->or
Operador-><
Operador->>
Operador-><=
Operador->>=
Operador->==
Operador-><>
Objeto->{ Elemento ListaObjetos }
Elemento->ε
ListaObjetos->, Expresion ListaObjetos
ListaObjetos->ε
Id->id IdCompuesto
IdCompuesto->IdValores
IdCompuesto->. Id
IdCompuesto->ε
IdValores->[ Expresion ListaValoresMatriz ]
ListaValoresMatriz->, Expresion ListaValoresMatriz
ListaValoresMatriz->ε
SubrutinasLista->BloqueSubrutinas SubrutinasLista
SubrutinasLista->ε
ArgumentosSubrutina->RefIndicador id MasTiposVar : TipoDato MasArgumentosSubrutina
ArgumentosSubrutina->ε
MasArgumentosSubrutina->; RefIndicador id MasTiposVar : TipoDato MasArgumentosSubrutina
MasArgumentosSubrutina->ε
RefIndicador->ref
RefIndicador->ε
RetornoOpcional->retorna TipoDato
RetornoOpcional->ε
BloqueSubrutinas->subrutina id ( ArgumentosSubrutina ) RetornoOpcional BloqueDeclaraciones inicio BloqueSentencias ListaSentencias fin
MasTiposVar->, id MasTiposVar
MasTiposVar->ε """.split("\n");




rules = [x.split("->") for x in grammarAngel];
i = 0

print(len(rules))
while(i != len(rules)-1):
    actual_rule = rules[i][0]
    index_rule = i;
    try:
        while(actual_rule == rules[i+1][0]):
            rules[index_rule].append(rules[i+1][1]);
            i+=1;
    except:
        continue;
    i+=1;

filter_rules = []
i = 0
while(i != len(rules)-1):

    actual_rule = rules[i][0]
    filter_rules.append(rules[i]);
    try:
        while(actual_rule == rules[i+1][0]):
            i+=1
        i+=1
    except:
        continue



for x in filter_rules:
    print(x);

izq,der = [x[0] for x in filter_rules],[x[1:] for x in filter_rules]


for x,y in zip(izq,der):
    print(x,"->",y)

print({x:y for x,y in zip(izq,der)})

#!/usr/bin/python
# -*- coding: utf-8 -*-
{
    'Programa': ['ProgramaFirma BloqueDeclaraciones inicio BloqueSentencias ListaSentencias fin SubrutinasLista'
                 ],
    'ProgramaFirma': ['programa id', '\xce\xb5'],
    'ListaDeclaraciones': ['Declaraciones ListaDeclaraciones',
                           '\xce\xb5'],
    'BloqueDeclaraciones': ['Declaraciones ListaDeclaraciones',
                            '\xce\xb5'],
    'Declaraciones': ['var id MasTiposVar : TipoDato FinSentencia ListaVarTipo'
                      ],
    'ListaConst': ['AsignacionConst FinSentencia ListaConst', '\xce\xb5'
                   ],
    'ListaVarTipo': ['id MasTiposVar : TipoDato FinSentencia ListaVarTipo'
                     , '\xce\xb5'],
    'TipoDato': ['TipoBasico', 'TipoComplejo'],
    'TipoBasico': ['numerico', 'cadena', 'logico', 'id'],
    'TipoComplejo': ['vector [ VectorTamanio ] TipoBasico',
                     'matriz [ MatrizTamanio ] TipoBasico',
                     'registro { ListaVarTipo }'],
    'VectorTamanio': ['VectorValor'],
    'MatrizTamanio': ['VectorValor MatrizTamanioLista'],
    'MatrizTamanioLista': [', MatrizTamanio', '\xce\xb5'],
    'VectorValor': ['*', 'Expresion'],
    'ListaArgumentos': [', Argumento ListaArgumentos', '\xce\xb5'],
    'CuerpoSi': ['ListaSentencias SinoSentenciaLista'],
    'SinoSiSentencia': ['si ( Expresion ) ListaSentencias'],
    'ListaSentencias': ['BloqueSentencias ListaSentencias', '\xce\xb5'
                        ],
    'BloqueSentencias': ['Sentencia FinSentencia'],
    'FinSentencia': ['\xce\xb5', ';'],
    'Sentencia': [
        'SentenciaAsignFunc',
        'SentenciaMientras',
        'SentenciaRepetirHasta',
        'SentenciaEval',
        'SentenciaDesde',
        'SentenciaRetorna',
        'SentenciaSi',
        ],
    'SentenciaSi': ['si ( Expresion ) { CuerpoSi }'],
    'SinoSentenciaLista': ['\xce\xb5',
                           'SinoSentencia SinoSentenciaLista'],
    'SinoSentencia': ['sino SinoSiSentencia'],
    'SentenciaMientras': ['mientras ( Expresion ) { ListaSentencias }'
                          ],
    'SentenciaRepetirHasta': ['repetir ListaSentencias hasta ( Expresion )'
                              ],
    'SentenciaEval': ['eval { EvalCuerpo ListaCasosEval SinoEval }'],
    'ListaCasosEval': ['EvalCuerpo ListaCasosEval', '\xce\xb5'],
    'EvalCuerpo': ['caso ( Expresion ) ListaSentencias'],
    'SinoEval': ['sino ListaSentencias', '\xce\xb5'],
    'SentenciaDesde': ['desde SentenciaAsignFunc hasta Expresion OpcionalPaso { ListaSentencias }'
                       ],
    'OpcionalPaso': ['paso Expresion', '\xce\xb5'],
    'SentenciaRetorna': ['retorna ( Expresion )'],
    'AsignacionConst': ['Id = Expresion'],
    'SentenciaAsignFunc': ['Id SentenciaId'],
    'SentenciaId': ['= Expresion', '( Argumento ListaArgumentos )'],
    'Argumento': ['Expresion', '\xce\xb5'],
    'Elemento': ['\xce\xb5'],
    'Expresion': ['NegacionOpcional ExpresionTerminal ExpresionOperador'
                  ],
    'ExpresionOperador': ['\xce\xb5'],
    'ExpresionFin': ['NegacionOpcional ExpresionTerminal ExpresionOperador'
                     ],
    'ExpresionTerminal': ['TRUE', 'FALSE', 'SI', 'NO', 'Objeto'],
    'NumIdTerminal': ['num', 'Id FuncionId'],
    'FuncionId': ['\xce\xb5', '( Argumento ListaArgumentos )'],
    'Signo': ['\xce\xb5', '+', '-'],
    'NegacionOpcional': ['not', '\xce\xb5'],
    'Operador': [
        '+',
        '-',
        '*',
        '/',
        '%',
        '^',
        'and',
        'or',
        '<',
        '>',
        '<=',
        '>=',
        '==',
        '<>',
        ],
    'Objeto': ['{ Elemento ListaObjetos }'],
    'ListaObjetos': [', Expresion ListaObjetos', '\xce\xb5'],
    'Id': ['id IdCompuesto'],
    'IdCompuesto': ['IdValores', '. Id', '\xce\xb5'],
    'IdValores': ['[ Expresion ListaValoresMatriz ]'],
    'ListaValoresMatriz': [', Expresion ListaValoresMatriz', '\xce\xb5'
                           ],
    'SubrutinasLista': ['BloqueSubrutinas SubrutinasLista', '\xce\xb5'
                        ],
    'ArgumentosSubrutina': ['RefIndicador id MasTiposVar : TipoDato MasArgumentosSubrutina'
                            , '\xce\xb5'],
    'MasArgumentosSubrutina': ['; RefIndicador id MasTiposVar : TipoDato MasArgumentosSubrutina'
                               , '\xce\xb5'],
    'RefIndicador': ['ref', '\xce\xb5'],
    'RetornoOpcional': ['retorna TipoDato', '\xce\xb5'],
    'BloqueSubrutinas': ['subrutina id ( ArgumentosSubrutina ) RetornoOpcional BloqueDeclaraciones inicio BloqueSentencias ListaSentencias fin'
                         ],
    'MasTiposVar': [', id MasTiposVar', '\xce\xb5 '],
    }
