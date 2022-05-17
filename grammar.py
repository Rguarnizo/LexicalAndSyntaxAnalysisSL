token = ""
tokens = []

def initSystaxAnalizer(init,ltokens):
  global token,tokens
  tokens = ltokens
  token = init
  GRAM()
def getToken():
  global token
  token = tokens.pop();
def errorSintaxis(token_esperado):
  token_esperado = ''.join([f" '{x}'," for x in sorted(token_esperado)])
  token_esperado = token_esperado[:-1]
  print(f"<{token.col}:{token.row}> Error sintactico: se encontro: '{token.valor if token.tipo == 'id' or token.tipo == 'tk_numero' else token.tipo}'; se esperaba:{token_esperado}.")
  quit()
  #raise Exception("Error Sintactico")
def emparejar(token_esperado):
  if token.tipo == token_esperado:
    getToken();
  else:
    errorSintaxis(token_esperado);
def GRAM():
  if token.tipo == "programa" or False:
    emparejar('programa')
    emparejar('id')
    A()
  elif token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or False:
    A()
  else:
    errorSintaxis(['programa', 'var', 'const', 'tipos', 'inicio']);
def A():
  if token.tipo == "const" or False:
    emparejar('const')
    C()
    A()
  elif token.tipo == "tipos" or False:
    emparejar('tipos')
    T()
    A()
  elif token.tipo == "var" or False:
    emparejar('var')
    V()
    A()
  elif token.tipo == "inicio" or False:
    P()
    S()
  else:
    errorSintaxis(['const', 'tipos', 'var', 'inicio']);
def C():
  if token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or token.tipo == "id" or False:
    CONST()
  else:
    errorSintaxis(['var', 'const', 'tipos', 'inicio', 'id']);
def T():
  if token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or token.tipo == "id" or False:
    TYPE()
  else:
    errorSintaxis(['var', 'const', 'tipos', 'inicio', 'id']);
def V():
  if token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or token.tipo == "id" or False:
    VAR()
  else:
    errorSintaxis(['var', 'const', 'tipos', 'inicio', 'id']);
def P():
  if token.tipo == "inicio" or False:
    emparejar('inicio')
    PROGRAM()
    emparejar('fin')
  else:
    errorSintaxis(['inicio']);
def S():
  if token.tipo == "subrutina" or False:
    emparejar('subrutina')
    SUB()
  elif token.tipo == "$" or False:
    print("El analisis sintactico ha finalizado exitosamente.")
    return
  else:
    errorSintaxis(['subrutina', '$']);
def CONST():
  if token.tipo == "id" or False:
    emparejar('id')
    emparejar('=')
    TCONST()
    OPTCOMMA()
    CONST()
  elif token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or False:
    return
  else:
    errorSintaxis(['id', 'var', 'const', 'tipos', 'inicio']);
def OPTCOMMA():
  if token.tipo == ";" or False:
    emparejar(';')
  elif token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or token.tipo == "id" or False:
    return
  else:
    errorSintaxis([';', 'var', 'const', 'tipos', 'inicio', 'id']);
def TCONST():
  if token.tipo == "tk_cadena" or False:
    emparejar('tk_cadena')
  elif token.tipo == "tk_numero" or False:
    emparejar('tk_numero')
  elif token.tipo == "tk_logico" or False:
    emparejar('tk_logico')
  else:
    errorSintaxis(['tk_cadena', 'tk_numero', 'tk_logico']);
def TYPE():
  if token.tipo == "id" or False:
    emparejar('id')
    emparejar(':')
    TTYPE()
    TYPE()
  elif token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or False:
    return
  else:
    errorSintaxis(['id', 'var', 'const', 'tipos', 'inicio']);
def TTYPE():
  if token.tipo == "numerico" or False:
    emparejar('numerico')
  elif token.tipo == "cadena" or False:
    emparejar('cadena')
  elif token.tipo == "logico" or False:
    emparejar('logico')
  elif token.tipo == "registro" or False:
    REG()
  elif token.tipo == "vector" or False:
    VEC()
  elif token.tipo == "matriz" or False:
    MATX()
  else:
    errorSintaxis(['numerico', 'cadena', 'logico', 'registro', 'vector', 'matriz']);
def VAR():
  if token.tipo == "id" or False:
    emparejar('id')
    OTHERSVARS()
  elif token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis(['id', 'var', 'const', 'tipos', 'inicio', '}']);
def OTHERSVARS():
  if token.tipo == "," or False:
    emparejar(',')
    emparejar('id')
    OTHERSVARS()
  elif token.tipo == ":" or False:
    VARTYPE()
  else:
    errorSintaxis([',', ':']);
def VARTYPE():
  if token.tipo == ":" or False:
    emparejar(':')
    TVAR()
    COMMAOPYC()
    VAR()
  else:
    errorSintaxis([':']);
def COMMAOPYC():
  if token.tipo == ";" or False:
    emparejar(';')
  elif token.tipo == "," or False:
    emparejar(',')
  elif token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or token.tipo == "id" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis([';', ',', 'var', 'const', 'tipos', 'inicio', 'id', '}']);
def TVAR():
  if token.tipo == "numerico" or False:
    emparejar('numerico')
  elif token.tipo == "id" or False:
    emparejar('id')
  elif token.tipo == "cadena" or False:
    emparejar('cadena')
  elif token.tipo == "logico" or False:
    emparejar('logico')
  elif token.tipo == "registro" or False:
    REG()
  elif token.tipo == "vector" or False:
    VEC()
  elif token.tipo == "matriz" or False:
    MATX()
  else:
    errorSintaxis(['numerico', 'id', 'cadena', 'logico', 'registro', 'vector', 'matriz']);
def VEC():
  if token.tipo == "vector" or False:
    emparejar('vector')
    emparejar('[')
    SVEC()
    emparejar(']')
    TVEC()
  else:
    errorSintaxis(['vector']);
def SVEC():
  if token.tipo == "*" or False:
    emparejar('*')
  elif token.tipo == "tk_numero" or False:
    emparejar('tk_numero')
  elif token.tipo == "id" or False:
    emparejar('id')
  else:
    errorSintaxis(['*', 'tk_numero', 'id']);
def TVEC():
  if token.tipo == "numerico" or False:
    emparejar('numerico')
  elif token.tipo == "cadena" or False:
    emparejar('cadena')
  elif token.tipo == "logico" or False:
    emparejar('logico')
  elif token.tipo == "id" or False:
    emparejar('id')
  elif token.tipo == "registro" or False:
    REG()
  else:
    errorSintaxis(['numerico', 'cadena', 'logico', 'id', 'registro']);
def MATX():
  if token.tipo == "matriz" or False:
    emparejar('matriz')
    emparejar('[')
    MATXARGS()
    emparejar(']')
    TMATX()
  else:
    errorSintaxis(['matriz']);
def MATXARGS():
  if token.tipo == "id" or token.tipo == "*" or token.tipo == "tk_numero" or False:
    TMATXARG()
    emparejar(',')
    TMATXARG()
    TMATX3()
  else:
    errorSintaxis(['id', '*', 'tk_numero']);
def TMATXARG():
  if token.tipo == "*" or False:
    emparejar('*')
  elif token.tipo == "tk_numero" or False:
    emparejar('tk_numero')
  elif token.tipo == "id" or False:
    emparejar('id')
  else:
    errorSintaxis(['*', 'tk_numero', 'id']);
def TMATX3():
  if token.tipo == "," or False:
    emparejar(',')
    TMATXARG()
  elif token.tipo == "]" or False:
    return
  else:
    errorSintaxis([',', ']']);
def TMATX():
  if token.tipo == "numerico" or False:
    emparejar('numerico')
  elif token.tipo == "cadena" or False:
    emparejar('cadena')
  elif token.tipo == "logico" or False:
    emparejar('logico')
  elif token.tipo == "id" or False:
    emparejar('id')
  elif token.tipo == "registro" or False:
    REG()
  else:
    errorSintaxis(['numerico', 'cadena', 'logico', 'id', 'registro']);
def REG():
  if token.tipo == "registro" or False:
    emparejar('registro')
    emparejar('{')
    NREG()
    emparejar('}')
  else:
    errorSintaxis(['registro']);
def NREG():
  if token.tipo == "id" or token.tipo == "}" or False:
    VAR()
  elif token.tipo == "{" or False:
    emparejar('{')
    NREG()
    emparejar('}')
  else:
    errorSintaxis(['id', '}', '{']);
def PROGRAM():
  if token.tipo == "eval" or token.tipo == "mientras" or token.tipo == "retorna" or token.tipo == "si" or token.tipo == "repetir" or token.tipo == "desde" or token.tipo == "id" or False:
    STCE()
    PROGRAM()
  elif token.tipo == "sino" or token.tipo == "caso" or token.tipo == "hasta" or token.tipo == "fin" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis(['eval', 'mientras', 'retorna', 'si', 'repetir', 'desde', 'id', 'sino', 'caso', 'hasta', 'fin', '}']);
def STCE():
  if token.tipo == "si" or False:
    emparejar('si')
    COND()
  elif token.tipo == "desde" or False:
    emparejar('desde')
    DESDE()
  elif token.tipo == "mientras" or False:
    emparejar('mientras')
    WHILE()
  elif token.tipo == "repetir" or False:
    emparejar('repetir')
    DOWHILE()
  elif token.tipo == "eval" or False:
    emparejar('eval')
    EVAL()
  elif token.tipo == "id" or False:
    emparejar('id')
    TIPOSCTE()
  elif token.tipo == "retorna" or False:
    RETORNA()
  else:
    errorSintaxis(['si', 'desde', 'mientras', 'repetir', 'eval', 'id', 'retorna']);
def TIPOSCTE():
  if token.tipo == "[" or token.tipo == "=" or token.tipo == "." or False:
    ASIG()
  elif token.tipo == "(" or False:
    FUNC()
    OPCOMMA()
  else:
    errorSintaxis(['[', '=', '.', '(']);
def ASIG():
  if token.tipo == "." or token.tipo == "=" or token.tipo == "[" or False:
    INDEX()
    POINT()
    emparejar('=')
    E()
    OPCOMMA()
  else:
    errorSintaxis(['.', '=', '[']);
def FUNC():
  if token.tipo == "(" or False:
    emparejar('(')
    ARGSFUNC()
    emparejar(')')
  else:
    errorSintaxis(['(']);
def OPCOMMA():
  if token.tipo == ";" or False:
    emparejar(';')
  elif token.tipo == "eval" or token.tipo == "mientras" or token.tipo == "retorna" or token.tipo == "si" or token.tipo == "sino" or token.tipo == "repetir" or token.tipo == "desde" or token.tipo == "caso" or token.tipo == "hasta" or token.tipo == "fin" or token.tipo == "id" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis([';', 'eval', 'mientras', 'retorna', 'si', 'sino', 'repetir', 'desde', 'caso', 'hasta', 'fin', 'id', '}']);
def ARGSFUNC():
  if token.tipo == "tk_cadena" or token.tipo == "not" or token.tipo == "tk_numero" or token.tipo == "{" or token.tipo == "tk_logico" or token.tipo == "(" or token.tipo == "id" or token.tipo == "-" or False:
    E()
    MARGSFUNC()
  elif token.tipo == ")" or False:
    return
  else:
    errorSintaxis(['tk_cadena', 'not', 'tk_numero', '{', 'tk_logico', '(', 'id', '-', ')']);
def MARGSFUNC():
  if token.tipo == "," or False:
    emparejar(',')
    E()
    MARGSFUNC()
  elif token.tipo == ")" or False:
    return
  else:
    errorSintaxis([',', ')']);
def ACCESS():
  if token.tipo == "[" or False:
    INDEX()
  elif token.tipo == "." or False:
    POINT()
  else:
    errorSintaxis(['[', '.']);
def INDEX():
  if token.tipo == "[" or False:
    emparejar('[')
    E()
    MINDEX()
    emparejar(']')
  elif token.tipo == "=" or token.tipo == "." or False:
    return
  else:
    errorSintaxis(['[', '=', '.']);
def MINDEX():
  if token.tipo == "," or False:
    emparejar(',')
    E()
    MINDEX()
  elif token.tipo == "]" or False:
    return
  else:
    errorSintaxis([',', ']']);
def POINT():
  if token.tipo == "." or False:
    emparejar('.')
    emparejar('id')
    MPOINTS()
  elif token.tipo == "=" or False:
    return
  else:
    errorSintaxis(['.', '=']);
def MPOINTS():
  if token.tipo == "." or False:
    emparejar('.')
    emparejar('id')
    MPOINTS()
  elif token.tipo == "=" or False:
    return
  elif token.tipo == "=" or token.tipo == "[" or False:
    INDEX()
  else:
    errorSintaxis(['.', '=', '=', '[']);
def E():
  if token.tipo == "tk_cadena" or token.tipo == "id" or token.tipo == "tk_logico" or token.tipo == "tk_numero" or False:
    TIPOT()
    EV()
  elif token.tipo == "(" or False:
    emparejar('(')
    E()
    emparejar(')')
    EV()
  elif token.tipo == "not" or token.tipo == "-" or False:
    ECHANGE()
    E()
  elif token.tipo == "{" or False:
    emparejar('{')
    EXPARR()
    emparejar('}')
  else:
    errorSintaxis(['tk_cadena', 'id', 'tk_logico', 'tk_numero', '(', 'not', '-', '{']);
def ECHANGE():
  if token.tipo == "-" or False:
    emparejar('-')
  elif token.tipo == "not" or False:
    emparejar('not')
  else:
    errorSintaxis(['-', 'not']);
def EV():
  if token.tipo == "+" or token.tipo == "*" or token.tipo == "^" or token.tipo == "or" or token.tipo == "/" or token.tipo == "%" or token.tipo == "tk_comparation" or token.tipo == "and" or token.tipo == "-" or False:
    OP()
    E()
  elif token.tipo == ";" or False:
    emparejar(';')
  elif token.tipo == ";" or token.tipo == "eval" or token.tipo == "]" or token.tipo == "mientras" or token.tipo == "{" or token.tipo == ")" or token.tipo == "sino" or token.tipo == "retorna" or token.tipo == "si" or token.tipo == "repetir" or token.tipo == "desde" or token.tipo == "caso" or token.tipo == "," or token.tipo == "hasta" or token.tipo == "fin" or token.tipo == "id" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis(['+', '*', '^', 'or', '/', '%', 'tk_comparation', 'and', '-', ';', ';', 'eval', ']', 'mientras', '{', ')', 'sino', 'retorna', 'si', 'repetir', 'desde', 'caso', ',', 'hasta', 'fin', 'id', '}']);
def TIPOT():
  if token.tipo == "id" or False:
    emparejar('id')
    TIPOID()
  elif token.tipo == "tk_numero" or False:
    emparejar('tk_numero')
  elif token.tipo == "tk_cadena" or False:
    emparejar('tk_cadena')
  elif token.tipo == "tk_logico" or False:
    emparejar('tk_logico')
  else:
    errorSintaxis(['id', 'tk_numero', 'tk_cadena', 'tk_logico']);
def TIPOID():
  if token.tipo == "[" or token.tipo == "." or False:
    ACCESS()
  elif token.tipo == "(" or False:
    FUNC()
  elif token.tipo == "+" or token.tipo == "*" or token.tipo == "or" or token.tipo == "mientras" or token.tipo == "sino" or token.tipo == "and" or token.tipo == "id" or token.tipo == "-" or token.tipo == "{" or token.tipo == ")" or token.tipo == "retorna" or token.tipo == "si" or token.tipo == "/" or token.tipo == "tk_comparation" or token.tipo == "fin" or token.tipo == ";" or token.tipo == "eval" or token.tipo == "repetir" or token.tipo == "hasta" or token.tipo == "}" or token.tipo == "^" or token.tipo == "]" or token.tipo == "desde" or token.tipo == "%" or token.tipo == "caso" or token.tipo == "," or False:
    return
  else:
    errorSintaxis(['[', '.', '(', '+', '*', 'or', 'mientras', 'sino', 'and', 'id', '-', '{', ')', 'retorna', 'si', '/', 'tk_comparation', 'fin', ';', 'eval', 'repetir', 'hasta', '}', '^', ']', 'desde', '%', 'caso', ',']);
def OP():
  if token.tipo == "*" or False:
    emparejar('*')
  elif token.tipo == "/" or False:
    emparejar('/')
  elif token.tipo == "+" or False:
    emparejar('+')
  elif token.tipo == "-" or False:
    emparejar('-')
  elif token.tipo == "%" or False:
    emparejar('%')
  elif token.tipo == "^" or False:
    emparejar('^')
  elif token.tipo == "tk_comparation" or False:
    emparejar('tk_comparation')
  elif token.tipo == "and" or False:
    emparejar('and')
  elif token.tipo == "or" or False:
    emparejar('or')
  else:
    errorSintaxis(['*', '/', '+', '-', '%', '^', 'tk_comparation', 'and', 'or']);
def EXPARR():
  if token.tipo == "{" or token.tipo == "}" or False:
    MULTROWS()
  elif token.tipo == "tk_cadena" or token.tipo == "{" or token.tipo == "tk_numero" or token.tipo == "}" or False:
    ACONST()
    MULTROWS()
  else:
    errorSintaxis(['{', '}', 'tk_cadena', '{', 'tk_numero', '}']);
def MULTROWS():
  if token.tipo == "{" or False:
    MATXARR()
    OTCOMMA()
    MULTROWS()
  elif token.tipo == "}" or False:
    return
  else:
    errorSintaxis(['{', '}']);
def OTCOMMA():
  if token.tipo == "," or False:
    emparejar(',')
  elif token.tipo == "{" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis([',', '{', '}']);
def MATXARR():
  if token.tipo == "{" or False:
    emparejar('{')
    ACONST()
    emparejar('}')
  else:
    errorSintaxis(['{']);
def ACONST():
  if token.tipo == "tk_cadena" or token.tipo == "tk_numero" or False:
    TARR()
    MACONST()
  elif token.tipo == "{" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis(['tk_cadena', 'tk_numero', '{', '}']);
def MACONST():
  if token.tipo == "," or False:
    emparejar(',')
    ACONST()
  elif token.tipo == "{" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis([',', '{', '}']);
def TARR():
  if token.tipo == "tk_cadena" or False:
    emparejar('tk_cadena')
  elif token.tipo == "tk_numero" or False:
    emparejar('tk_numero')
  else:
    errorSintaxis(['tk_cadena', 'tk_numero']);
def DESDE():
  if token.tipo == "id" or False:
    DES()
    emparejar('hasta')
    M()
    PASO()
    emparejar('{')
    PROGRAM()
    emparejar('}')
  elif token.tipo == "eval" or token.tipo == "mientras" or token.tipo == "retorna" or token.tipo == "si" or token.tipo == "sino" or token.tipo == "repetir" or token.tipo == "desde" or token.tipo == "caso" or token.tipo == "hasta" or token.tipo == "fin" or token.tipo == "id" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis(['id', 'eval', 'mientras', 'retorna', 'si', 'sino', 'repetir', 'desde', 'caso', 'hasta', 'fin', 'id', '}']);
def DES():
  if token.tipo == "id" or False:
    emparejar('id')
    MANAGEDES()
  else:
    errorSintaxis(['id']);
def MANAGEDES():
  if token.tipo == "=" or False:
    emparejar('=')
    TIPOM()
  else:
    errorSintaxis(['=']);
def M():
  if token.tipo == "id" or False:
    emparejar('id')
    MANAGEIDM()
  elif token.tipo == "tk_numero" or False:
    emparejar('tk_numero')
  else:
    errorSintaxis(['id', 'tk_numero']);
def MANAGEIDM():
  if token.tipo == "(" or False:
    emparejar('(')
    ARGSFUNC()
    emparejar(')')
  elif token.tipo == "+" or token.tipo == "*" or token.tipo == "^" or token.tipo == "or" or token.tipo == "/" or token.tipo == "%" or token.tipo == "tk_comparation" or token.tipo == "and" or token.tipo == "-" or False:
    OP()
    TIPOM()
  elif token.tipo == "{" or token.tipo == "paso" or False:
    return
  else:
    errorSintaxis(['(', '+', '*', '^', 'or', '/', '%', 'tk_comparation', 'and', '-', '{', 'paso']);
def TIPOM():
  if token.tipo == "tk_numero" or False:
    emparejar('tk_numero')
  elif token.tipo == "id" or False:
    emparejar('id')
  else:
    errorSintaxis(['tk_numero', 'id']);
def PASO():
  if token.tipo == "paso" or False:
    emparejar('paso')
    E()
  elif token.tipo == "{" or False:
    return
  else:
    errorSintaxis(['paso', '{']);
def COND():
  if token.tipo == "(" or False:
    emparejar('(')
    E()
    emparejar(')')
    emparejar('{')
    SINOSI()
    PROGRAMSI()
    emparejar('}')
  else:
    errorSintaxis(['(']);
def SINOSI():
  if token.tipo == "sino" or False:
    emparejar('sino')
    SI()
  elif token.tipo == "id" or token.tipo == "sino" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis(['sino', 'id', 'sino', '}']);
def SI():
  if token.tipo == "id" or token.tipo == "sino" or token.tipo == "}" or False:
    PROGRAMSI()
  elif token.tipo == "si" or False:
    emparejar('si')
    E()
    PROGRAMSI()
  else:
    errorSintaxis(['id', 'sino', '}', 'si']);
def PROGRAMSI():
  if token.tipo == "id" or token.tipo == "sino" or False:
    STCESI()
    PROGRAMSI()
  elif token.tipo == "id" or token.tipo == "sino" or token.tipo == "}" or False:
    return
  else:
    errorSintaxis(['id', 'sino', 'id', 'sino', '}']);
def STCESI():
  if token.tipo == "id" or False:
    emparejar('id')
    TIPOSCTE()
  elif token.tipo == "id" or token.tipo == "sino" or token.tipo == "}" or False:
    SINOSI()
  else:
    errorSintaxis(['id', 'id', 'sino', '}']);
def LOOPS():
  if token.tipo == "(" or False:
    WHILE()
  elif token.tipo == "hasta" or False:
    DOWHILE()
  elif False:
    return
  else:
    errorSintaxis(['(', 'hasta']);
def WHILE():
  if token.tipo == "(" or False:
    emparejar('(')
    E()
    emparejar(')')
    emparejar('{')
    PROGRAM()
    emparejar('}')
  else:
    errorSintaxis(['(']);
def DOWHILE():
  if token.tipo == "eval" or token.tipo == "mientras" or token.tipo == "retorna" or token.tipo == "si" or token.tipo == "repetir" or token.tipo == "desde" or token.tipo == "hasta" or token.tipo == "id" or False:
    PROGRAM()
    emparejar('hasta')
    emparejar('(')
    E()
    emparejar(')')
  else:
    errorSintaxis(['eval', 'mientras', 'retorna', 'si', 'repetir', 'desde', 'hasta', 'id']);
def EVAL():
  if token.tipo == "{" or False:
    emparejar('{')
    MEVAL()
    emparejar('sino')
    PROGRAM()
    emparejar('}')
  else:
    errorSintaxis(['{']);
def MEVAL():
  if token.tipo == "caso" or False:
    emparejar('caso')
    emparejar('(')
    E()
    emparejar(')')
    PROGRAM()
    MEVAL()
  elif token.tipo == "sino" or False:
    return
  else:
    errorSintaxis(['caso', 'sino']);
def RETORNA():
  if token.tipo == "retorna" or False:
    emparejar('retorna')
    emparejar('(')
    E()
    emparejar(')')
  else:
    errorSintaxis(['retorna']);
def SUB():
  if token.tipo == "id" or False:
    emparejar('id')
    emparejar('(')
    SUBARG()
    emparejar(')')
    RET()
    A()
  elif token.tipo == "$" or False:
    print("El analisis sintactico ha finalizado exitosamente.")
    return
  else:
    errorSintaxis(['id', '$']);
def RET():
  if token.tipo == "retorna" or False:
    emparejar('retorna')
    TSUBARG()
  elif token.tipo == "var" or token.tipo == "const" or token.tipo == "tipos" or token.tipo == "inicio" or False:
    return
  else:
    errorSintaxis(['retorna', 'var', 'const', 'tipos', 'inicio']);
def SUBRUTINE():
  if token.tipo == "inicio" or False:
    emparejar('inicio')
    PROGRAM()
    emparejar('fin')
  else:
    errorSintaxis(['inicio']);
def SUBARG():
  if token.tipo == "id" or False:
    SUBMID()
    emparejar(':')
    TSUBARG()
    MSUBARG()
  elif token.tipo == "ref" or False:
    emparejar('ref')
    SUBMID()
    emparejar(':')
    TSUBARG()
    MSUBARG()
  elif token.tipo == ")" or False:
    return
  else:
    errorSintaxis(['id', 'ref', ')']);
def SUBMID():
  if token.tipo == "id" or False:
    emparejar('id')
    OTHERID()
  else:
    errorSintaxis(['id']);
def OTHERID():
  if token.tipo == "," or False:
    emparejar(',')
    emparejar('id')
    OTHERID()
  elif token.tipo == ":" or False:
    return
  else:
    errorSintaxis([',', ':']);
def MSUBARG():
  if token.tipo == ";" or False:
    emparejar(';')
    SUBARG()
  elif token.tipo == ")" or False:
    return
  else:
    errorSintaxis([';', ')']);
def TSUBARG():
  if token.tipo == "numerico" or False:
    emparejar('numerico')
  elif token.tipo == "cadena" or False:
    emparejar('cadena')
  elif token.tipo == "logico" or False:
    emparejar('logico')
  elif token.tipo == "id" or False:
    emparejar('id')
  elif token.tipo == "vector" or False:
    VEC()
  elif token.tipo == "matriz" or False:
    MATX()
  else:
    errorSintaxis(['numerico', 'cadena', 'logico', 'id', 'vector', 'matriz']);
