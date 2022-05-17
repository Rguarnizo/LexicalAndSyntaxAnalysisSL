def match(tup,target):
   if len(tup) != len(target):
      return False
   for i in range(len(tup)):
      if target[i] != "*" and tup[i] != target[i]:
         return False
   return True

def get_tuples(mydict,target):
   keys = filter(lambda x: match(x,target),mydict.keys())
   return [mydict[key] for key in keys]

def gen_grammar_code(prediccion,izq,der,debug = 1):



  with open("grammar.py", "w") as o:
    o.write('''token = ""
tokens = []

def initSystaxAnalizer(init,ltokens):
  global token,tokens
  tokens = ltokens
  token = init
  GRAM()\n''')
    o.write('''def getToken():
  global token
  token = tokens.pop();\n''')
    
    o.write('''def errorSintaxis(token_esperado):\n''');
    o.write('''  token_esperado = ''.join([f" '{x}'," for x in sorted(token_esperado)])\n''')
    o.write('''  token_esperado = token_esperado[:-1]\n''')
    o.write('''  print(f"<{token.col}:{token.row}> Error sintactico: se encontro: '{token.valor if token.tipo == 'id' or token.tipo == 'tk_numero' else token.tipo}'; se esperaba:{token_esperado}.")
  quit()
  #raise Exception("Error Sintactico")\n''')
    o.write(f'''def emparejar(token_esperado):
  if token.tipo == token_esperado:
    getToken();
  else:
    errorSintaxis(token_esperado);\n''')


    for x,y in zip(izq,der):
      rules = y.split("|")
      o.write(f'''def {x}():\n''')
      if debug:
        o.write(f'''  print(token.col,token.row,'{x}',token.tipo,token.valor)\n''')
      predictions = []
      
      for i,rule in enumerate(rules):
        preds = get_tuples(prediccion,(x,rule))[0]['Prediccion']
        if i == 0:
          o.write(f'''  if ''')
        else:
          o.write(f'''  elif ''')
          
        for pred in preds:
          predictions.append(pred);            
          o.write(f'''token.tipo == "{pred}" or ''')
        o.write(f'''False:\n''')
        nts = rule.split(" ")
        if debug:
          o.write(f'''    print({nts})\n''');
        for nt in nts:
          if(pred in ['$']):
            o.write(f'''    print("El analisis sintactico ha finalizado exitosamente.")\n''')
          if(nt in ['""']):
            o.write(f'''    return\n''')
            break
          elif(nt.isupper()):
            o.write(f'''    {nt}()\n''')
          else:
             o.write(f'''    emparejar('{nt}')\n''')
      o.write(f'''  else:
    errorSintaxis({predictions});\n''')