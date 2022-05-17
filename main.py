#!/usr/bin/env python3

import sys
from LexicalAnalyzer.lexical_analizer import tokenAnalizer
from SyntaxAnalyzer.predictions import *
from grammar import *

try:
    file = sys.argv[1]
except:
    file = None
tokens = tokenAnalizer(f"TestCases/{sys.argv[1]}.in" if file else None)
tokens.reverse()
token = tokens.pop()

initSystaxAnalizer(token, tokens)