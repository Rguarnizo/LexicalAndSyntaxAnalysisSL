def gram_to_str(gramm):
  grammar = ''
  for x,y in gramm.items():
    grammar += f'''{x}->{ ' '.join(y) if isinstance(y,list) else'|'.join([' '.join(r) for r in y])}\n'''
  return grammar