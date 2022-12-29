'''
  Este é um programa do algoritmo genético de Holland
  para encontrar o número binário dentre do intervalo de 
  [0,255] que apresenta a maior ocorrência da sub string 01
  * a população é formada por 10 cromossomo 
  * o cromossomo é um vetor binário de 8 posições 
  * cruzamento de um ponto de corte e probabilidade de cruzamento maior que 60
  * mutação por complemento com probabilidade de mutação maior que 90
  * inversão com probabilidade de inversão de 90
  * seleção e substituição elitista
'''

import random as rd

# gera a população
def gera_pop_in(populacao):
  for i in range(10):
    cromossomo = []
    for j in range(8):
      cromossomo.append(rd.randint(0, 1))
    populacao.append(cromossomo)

# mostra a população
def mostra_pop(populacao):
  for i in range(len(pop)):
    print(populacao[i])

# atribui valor de adaptação para cada cromossomo da população
def adaptacao(adaptPop, populacao):
  adaptacao = 0
  for i in range(len(populacao)):
    for j in range(len(populacao[i]) - 1):
      if populacao[i][j] == 0 and populacao[i][j + 1] == 1:
        adaptacao += 1
    adaptPop.append(adaptacao)
    adaptacao = 0

# mostra população com o valor de adaptação
def mostra_pop_adapt(adaptPop, populacao):
  for i in range(len(populacao)):
    print(adaptPop[i], " = ", populacao[i])

# ordena a população com base no valor de adaptação de cada cromossomo
def ordena_pop(adaptPop, populacao):
  for i in range(len(populacao)):
    for j in range(len(populacao) - 1):
      if adaptPop[i] > adaptPop[j]:
        aux1 = adaptPop[i]
        adaptPop[i] = adaptPop[j]
        adaptPop[j] = aux1

        aux2 = populacao[i]
        populacao[i] = populacao[j]
        populacao[j] = aux2

# cruza cromossomos dado um ponto de corte aleatório
def cruzamento(populacao, descendentes):
  # pega apenas os 5 primeiros cromossomos da população para usar no cruzamento
  filho1 = []
  filho2 = []
  for i in range(5):
    for j in range(5):
      x = rd.randint(1, 100)
      if x > 60 and len(descendentes) <= 28:
        corte = rd.randint(1, 7)
        pai = populacao[i]
        mae = populacao[j]
        if i != j:
          # adiciona os primeiro genes aos cromossomos filhos
          for k in range(corte):
            filho1.append(pai[k])
            filho2.append(mae[k])

          # adiciona os últimos genes aos cromossomos filhos
          for l in range(len(pai) - corte):
            filho1.append(mae[l + corte])
            filho2.append(pai[l + corte])

          descendentes.append(filho1)
          descendentes.append(filho2)
          filho1 = []
          filho2 = []

def mutacao(populacao, descendentes):
  for i in range(5):
    x = rd.randint(1, 100)
    if len(descendentes) <= 29 and x > 90:
      for j in range(8):
        x = rd.randint(0, 1)
        if x == 0:
          if populacao[i][j] == 0:
            descendentes[i][j] = 1
          else:
            descendentes[i][j] = 0
        else:
            descendentes[len(descendentes) - 1][j] = populacao[i][j]

def inversao(populacao, descendentes):
  for a in range(5):
    x = rd.randint(1, 100) # probabilidade de inversão é maior do que 90
    if  x > 90 and len(descendentes) <= 29:
      for b in range(8):
        descendentes[len(descendentes)][b] = populacao[a][b]
      p1 = rd.randint(0, 6)	# escolhe a primeira posição
      p2 = rd.randint(0, 7)						
      while p2 < p1: # escolhe a segunda posição, onde p1 < p2
        p2 = rd.randint(0, 7)
      x = int((p2 - p1) / 2)
      for b in range(x): # inverte o conteúdo do cromossomo entre p1 e p2
        aux = descendentes[len(descendentes)][p1 + b]
        descendentes[len(descendentes)][p1 + b] = descendentes[len(descendentes)][p2 - b]
        descendentes[len(descendentes)][p2 - b] = aux

def substituicao(populacao, adaptPop, descendentes, adaptDes):
  novaPopulacao = populacao
  novoAdaptDes = adaptDes
  b = 0 # índice da população atual
  c = 0 # índice da população de descendentes
  for a in range(10): # índice da nova população
    if b <= 10 and c <= len(descendentes):
      if adaptPop[b] > adaptDes[c]:
        for i in range(8):
          novaPopulacao[a][i] = populacao[b][i]
        novoAdaptDes[a] = adaptPop[b]
        b += 1
      else:
        for i in range(8):
          novaPopulacao[a][i] = descendentes[c][i]
        novoAdaptDes[a] = adaptDes[c]
        c += 1
    else:
      if b <= 10 and c > len(des):
        for i in range(8):
          novaPopulacao[a][i] = populacao[b][i]
        novoAdaptDes[a] = adaptPop[b]
        b += 1
      
      else:
        for i in range(8):
          novaPopulacao[a][i] = descendentes[c][i]
        novoAdaptDes[a] = adaptDes[c]
        c += 1
  
  for a in range(10):
    for i in range(8):
      pop[a][i] = novaPopulacao[a][i]
    adaptPop[a] = novoAdaptDes[a]
  
  return novaPopulacao, novoAdaptDes


pop = []
adapt = []
des = []
adaptDes= []
aux = []
nP = []
nA = []

print("\n--- População atual gerada ---\n")
gera_pop_in(pop)
mostra_pop(pop)

print("\n--- População atual com sua adaptação ---\n")
adaptacao(adapt, pop)
mostra_pop_adapt(adapt, pop)

print("\n--- População atual na ordem decrescente da adaptação ---\n")
ordena_pop(adapt, pop)
mostra_pop_adapt(adapt, pop)

while adapt[0] != 4:
  print("\n--- Cruzamento ---\n")
  cruzamento(pop, des)
  mostra_pop(des)

  print("\n--- Mutação ---\n")
  mutacao(pop, des)
  mostra_pop(des)

  print("\n--- Inversao ---\n")
  inversao(pop, des)
  mostra_pop(des)

  print("\n--- População descencente com sua adaptação ---\n")
  adaptacao(adaptDes, des)
  mostra_pop_adapt(adaptDes, des)

  print("\n--- População descendente na ordem decrescente da adaptação ---\n")
  ordena_pop(adaptDes, des)
  mostra_pop_adapt(adaptDes, des)

  print("\n--- População nova ---\n")
  nP, nA = substituicao(pop, adapt, des, adaptDes)
  ordena_pop(nA, nP)
  mostra_pop_adapt(nA, nP)
