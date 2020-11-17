# ------------------------------------------------------------
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
# List of token names. This is always required
tokens = ('mision','si','sino','pinocho','numero','lnumero','decimal','ldecimal','mostrar','texto','ltexto','descansito','yoyo','devuelve','chacha','lchacha','mas','menos','por','y','o','dividir','mayor','menor','pizquierdo','pderecho','cizquierdo','cderecho','coma','igual','menor_igual','mayor_igual','diferente','identificador','lizquierdo','lderecho','division','verdad','mentira','modulo','llama')

# Regular expression rules for simple tokens
t_mision = r'mision'
t_si = r'si'
t_sino = r'sino'
t_pinocho = r'pinocho'
t_numero = r'numero'
t_decimal = r'decimal'
t_mostrar = r'mostrar'
t_texto = r'texto'
t_descansito = r'descansito'
t_yoyo = r'yoyo'
t_devuelve = r'devuelve'
t_chacha = r'chacha'
t_llama = r'llama'

t_mas = r'\+'
t_menos = r'\-'
t_por = r'\*'
t_division = r'\/'
t_modulo = r'\%'

t_y = r'\#y'
t_o = r'\#o'

t_mayor = r'\>'
t_menor = r'\<'

t_pizquierdo = r'\('
t_pderecho = r'\)'

t_lizquierdo = r'\{'
t_lderecho = r'\}'

t_cizquierdo = r'\['
t_cderecho = r'\]'

t_coma = r'\,'
t_igual = r'\='
t_menor_igual = r'\<\='
t_mayor_igual = r'\>\='
t_diferente = r'\<\>'

def t_identificador(t):
  r'(?!decimal|si|sino|pinocho|numero|mostrar|texto|descansito|yoyo|devuelve|chacha|mision|mentira|verdad|llama)[a-zA-Z]+[\w]*'
  try:
    t.value = t.value
  except ValueError:
    t.value = 0
  return t



# A regular expression rule with some action code
def t_mentira(t):
  r'mentira'
  t.value = False # guardamos el valor del lexema
  return t

def t_verdad(t):
  r'verdad'
  t.value = True # guardamos el valor del lexema
  return t

def t_lnumero(t):
  r'\d+(?!\.)'
  try:
    t.value = int(t.value) # guardamos el valor del lexema
  except ValueError:
    t.value = 0
  return t

def t_ldecimal(t):
  r'(0|[1-9][0-9]*)\.[0-9]*'
  try:
    t.value = float(t.value)
  except ValueError:
    t.value = 0
  return t

def t_lchacha(t):
  r'\'(\W|\w)\''
  t.value = t.value # guardamos el valor del lexema
  return t

def t_ltexto(t):
  r'\"(\W|\w)+\"'
  t.value = t.value # guardamos el valor del lexema
  return t

def t_comments(t):
    r'\~(\w|\W)*\~'

# Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
# Build the lexer
lexer = lex.lex()
# Test it out

file=open('archivo.txt','r')
texto=file.readlines()
file.close()
data = texto
tokens=[]
tokens_info=[]
for renglon in texto:
  # Give the lexer some input
  lexer.input(renglon)
  # Tokenize
  while True:
    tok = lexer.token()
    if not tok:
      break # No more input
    tokens.append(tok.type)
    tokens_info.append(tok)
    #print(tok.type, tok.value, tok.lineno, tok.lexpos)