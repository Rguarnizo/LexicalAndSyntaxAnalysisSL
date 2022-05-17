from token import *
from .transiciones import *
from .type_tokens import *
from .type import *

def tokenAnalizer(file):
    import sys
    if file:
        input = open(file).read();
    else:
        input = sys.stdin.read();

    input = input.split('\n')
    global tokens

    state = 0
    row = 0
    col = 0
    err = False
    token = ""
    tokens = []

    for row, line in enumerate(input):
        line = line + " "
        len_l = len(line)

        if len_l == 0:
            continue

        col = 0

        while(col != len_l):
            if(state == 0):
                if(token not in ["", " ","\t"]
                   and not token.startswith('//')
                   and not token.startswith('/*')):
                    result, err = type_token(
                        token, row if col == 0 else row+1, col-len(token)+1)
                    tokens.append(result)
                    if err:
                        break

                token = ""

            char = line[col]

            state, corr = transiciones[(state, type(char, state)[0])]

            if(corr != 0):
                col = col - corr
            else:
                token = token + char

            col += 1

        if(token[0] in ["'", '"'] and token[-1] not in ["'", '"']):
            tokens.append(type_token('!', row if col ==
                          0 else row+1, col-len(token)+1)[0])
            break

        row += 1
        col = 0

        if err:
            break

        if(not token.startswith('/*')):
            state = 0
    
    tokens.append(Token('$',0,0))
    return tokens
