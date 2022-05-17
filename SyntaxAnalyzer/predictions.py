from .gen_grammar_code import *
from .grammar import *
from .grammar_to_str import *
from .grammar_to_antr import *

Prediccion = {}

def alpha(nt,ls,grammar):
  if not ls:
    return 
  if not ls[0].isupper():
    Prediccion[nt]['Primeros'].append(ls[0])
  else:
    Prediccion[nt]['Primeros'].append(ls[0])
    if('""' in grammar[ls[0]]):
      alpha(nt,ls[1:],grammar)

def primeros (produccion):
  izq = [x[0] for x in produccion][::-1]
  der = [x[1] for x in produccion][::-1]

  reglas = [x.split("|") for x in der]

  grammar = dict(zip(izq,reglas))
  

  for nt,t in zip(izq,reglas):
    Prediccion[nt] = {}
    Prediccion[nt]['Primeros'] = []
    Prediccion[nt]['Reglas'] = t
    for rule in t:
      pr = rule.split(" ")
      alpha(nt,pr,grammar)
  
  for nt in izq:
    primeros = Prediccion[nt]['Primeros']
    for t in primeros:
      if t.isupper():
        primeros_t = Prediccion[t]['Primeros']
        Prediccion[nt]['Primeros'] = primeros_t + Prediccion[nt]['Primeros']

  for nt in izq:
    Prediccion[nt]['Primeros'] = set([x for x in Prediccion[nt]['Primeros'] if not x.isupper()])
  
  try:
    Prediccion[izq[-1]]['Primeros'].remove('""')
  except:
    pass

def sgte(nt,ls,grammar):
  if not ls:
    return 
  if not ls[0].isupper():
    Prediccion[nt]['Siguientes'].append(ls[0])
  else:
    Prediccion[nt]['Siguientes'].append(ls[0])
    if('""' in grammar[ls[0]]):
      sgte(nt,ls[1:],grammar)

def siguientes(produccion):
  izq = [x[0] for x in produccion]
  der = [x[1] for x in produccion]
  reglas = [x.split("|") for x in der]
  grammar = dict(zip(izq,reglas))


  for x in izq:
    Prediccion[x]['Siguientes'] = []
    Prediccion[x]['Right'] = []
    Prediccion[x]['Sgte'] = []
    
  Prediccion[izq[0]]['Siguientes'].append("$")

  change = True

  for x,y in zip(izq,der):
    rules = y.split("|")
    for rule in rules:    
      nts = rule.split(" ")
      for nt in nts:
        if nt.isupper():
          Prediccion[nt]["Right"].append((nts,x)) 

  
  
  for x in izq:
    rules = Prediccion[x]["Right"]
    for rule,fr in rules:
      i = rule.index(x)
      if (rule[i+1:]):
        k=1
        sgte(x,rule[i+k:],grammar)
        try:
          while(rule[i+k].isupper() and ('""' in grammar[rule[i+k]])):
            sgte(x,rule[i+k:],grammar)
            k+=1
        except:
            Prediccion[x]['Sgte'].append(fr)
      else:
        Prediccion[x]['Sgte'].append(fr)


  for nt in izq:
    primeros = Prediccion[nt]['Siguientes']
    for t in primeros:
      if t.isupper():
        primeros_t = Prediccion[t]['Primeros']
        Prediccion[nt]['Siguientes'] = list(primeros_t) + list(Prediccion[nt]['Siguientes'])
  
  for nt in izq:
    Prediccion[nt]['Siguientes'] = [x for x in Prediccion[nt]['Siguientes'] if not x.isupper()]

  for x in izq:
    sgtes = Prediccion[x]['Sgte']
    for y in sgtes:
      Prediccion[x]['Siguientes'] = list(Prediccion[y]['Siguientes']) + Prediccion[x]['Siguientes']

  for nt in izq:
    Prediccion[nt]['Siguientes'] = set([x for x in Prediccion[nt]['Siguientes'] if not x.isupper() and x not in'""'])


def pmroalpha(nt,ls,rule,grammar):
  if not ls:
    Prediccion[(nt,rule)]['Prediccion'].append('""')
    return 
  if not ls[0].isupper():
    Prediccion[(nt,rule)]['Prediccion'].append(ls[0])
  else:
    Prediccion[(nt,rule)]['Prediccion'].append(ls[0])
    if('""' in grammar[ls[0]]):
      pmroalpha(nt,ls[1:],rule,grammar)

def prediccion(produccion):
  izq = [x[0] for x in produccion]
  der = [x[1] for x in produccion]
  reglas = [(x.split("|")) for x in der]
  grammar = dict(zip(izq,reglas))

  for x,y in zip(izq,reglas):
    for rule in y:
      ls = rule.split(" ")
      Prediccion[(x,rule)] = {}
      Prediccion[(x,rule)]['Prediccion'] = []
      pmroalpha(x,ls,rule,grammar)
      for nt in Prediccion[(x,rule)]['Prediccion']:
        if(nt.isupper()):
          Prediccion[(x,rule)]['Prediccion'] += list(Prediccion[nt]['Primeros'])     
          try:
            Prediccion[(x,rule)]['Prediccion'].remove('""')
          except:
            pass
      if '""' in Prediccion[(x,rule)]['Prediccion']:
        Prediccion[(x,rule)]['Prediccion'] += list(Prediccion[x]['Siguientes'])
        Prediccion[(x,rule)]['Prediccion'].remove('""')
        

  for x,y in zip(izq,reglas):
      for rule in y:
        Prediccion[(x,rule)]['Prediccion'] = set(Prediccion[(x,rule)]['Prediccion'])
        try:
          Prediccion[(x,rule)]['Prediccion'].remove('""')
        except:
          pass
        Prediccion[(x,rule)]['Prediccion'] = set([nt for nt in Prediccion[(x,rule)]['Prediccion'] if not nt.isupper()])


grammar = gram_to_str(Gramatica).split("\n")
grammar_antr = grammar_to_antr(Gramatica)
productions = [x.split("->") for x in grammar]
productions.pop()
primeros(productions)
siguientes(productions)
prediccion(productions)

izq = [x[0] for x in productions]
der = [x[1] for x in productions]

gen_grammar_code(Prediccion,izq,der,debug=0)