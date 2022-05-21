import re
import cProfile
import timeit

# criação de uma linha com palavras aleatórias
line = 'let\'s say this is a random line for test purposes, and that I\'m going to parse through and find some random pattern'

pattern = re.compile(r'say') # compilação de um determinado padrão que queremos encontrar na linha acima
match = re.search(pattern, line) # pré condição para evitar a repetição no loop

# condition = 4 > 5 # condições alternativas
# condition_inv = 4 <= 5 # condições alternativas

a = 200 # tamanho do array A x A
arr = [[0]*a]*a # array com os A x A valores inicializados com o  valor 0
b = 0 # variável para calculo na condicional "else"
c = 0 # variável para calculo na condicional "else"

# função original com verificação da condição a cada iteração
def orig():
  for i in range(0, a):
    for j in range(0, a):
      if(re.search(r"say", line)): # veirifcação a cada iteração
      # if(4 > 5):
        arr[i][j] = (i * j) + i
      else:
        b = 5.4 * i
        c = b + 6.496


# função original com verificação da condição invertida a cada iteração
def orig_inv():
  for i in range(0, a):
    for j in range(0, a):
      if(not(re.search(r"say", line))):# veirifcação invertida a cada iteração
      # if(4<= 5):
        arr[i][j] = (i * j) + i
      else:
        b = 5.4 * i
        c = b + 6.496

# função alternativa com verificação da condição feita previamente
def alternated():
  for i in range(0, a):
    for j in range(0, a):
      # if(condition):
      if(match): # resultado da condicional salva
        arr[i][j] = (i * j) + i
      else:
        b = 5.4 * i
        c = b + 6.496

# função alternativa com verificação invertida da condição feita previamente
def alternated_inv():
  for i in range(0, a):
    for j in range(0, a):
      # if(condition_inv):
      if(not match): # resultado da condicional salva invertida
        arr[i][j] = (i * j) + i
      else:
        b = 5.4 * i
        c = b + 6.496

# execução de todas as funções, medindo seus tempos de execução
def execute():
  print('Original: ', timeit.timeit('orig()', 'from __main__ import orig', number=1000))
  print('Original inversa: ', timeit.timeit('orig_inv()', 'from __main__ import orig_inv', number=1000))
  print('Alternated: ', timeit.timeit('alternated()', 'from __main__ import alternated', number=1000))
  print('Alternated inversa: ', timeit.timeit('alternated_inv()', 'from __main__ import alternated_inv', number=1000))

# geração do arquivo profile
cProfile.run('execute()', filename='main.prof')

# snakeviz filename.prof para ver o gráfico