import cProfile
import random
import time
import timeit

# versão original
# o algoritmo cria um intervalo cujo tamanho é a metade do
# tamanho do array e compara os valores de cada item com o próximo
# valor após o intervalo.
def shellSort(arr):
  gap = len(arr) // 2

  while gap > 0: # critério de parada
    i = 0
    j = gap
      
    
    while j < len(arr): # loop
      if arr[i] >arr[j]: 
        arr[i],arr[j] = arr[j],arr[i] # swap dos itens a direita que sejam menores
        
      i += 1
      j += 1
    
      k = i
      while k - gap > -1: # loop
        if arr[k - gap] > arr[k]:
            arr[k-gap],arr[k] = arr[k],arr[k-gap] # swap dos itens a direita que sejam menores
        k -= 1

    gap //= 2 # reduz o intervalo

# versão melhorada que apresenta uma mesclagem de loops
def shellSort2(arr, size):

  j = None
  gap = size / 2

  while gap > 0: # critério de parada
    for i in range(round(gap), size):
      temp = arr[i]
      j = i

      # Mesclagem do loops das linas 13 e 26
      while j >= gap and temp < arr[round(j) - round(gap)]:
        arr[round(j)] = arr[round(j) - round(gap)] # swap dos itens a direita que sejam menores
        j -= gap

      arr[round(j)] = temp
    gap /= 2 # reduz o intervalo

# main onde o todo o codigo é executado
def execute_shell():
  lista = [random.randint(0, 100) for i in range(10000)] # gerando lista aleatoria
  copy = lista[:]

  t1 = time.time()
  shellSort(copy) # chamando o original
  t2 = time.time()

  print("Shell original took : %s seconds to complete" % (t2 - t1))

  copy = lista[:]

  t1 = time.time()
  shellSort2(copy, len(copy)) # chamando o otimizado
  t2 = time.time()

  print("Shell otimizado took : %s seconds to complete" % (t2 - t1))

# ferramenta de profile
cProfile.run("execute_shell()", filename='shells.prof')
# snakeviz filename.prof para visualizar o gráfico
 