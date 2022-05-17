def grammar_to_antr(gramm):
    grammar = ''
    for x, y in gramm.items():
        grammar += f'''{x.lower()}:{ ' '.join([el.upper() if el.islower() else el.lower() for el in y]) if isinstance(y,list) else'|'.join([' '.join([el.upper() if el.islower() else el.lower() for el in r]) for r in y])};\n'''
    return grammar
