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
def gera_pop_in(pop):
  for i in range(10):
    cromossomo = []
    for j in range(8):
      cromossomo.append(rd.randint(0, 1))
    pop.append(cromossomo)

# mostra a população
def mostra_pop(pop):
  for i in range(len(pop)):
    print(pop[i])

# atribui valor de adaptação para cada cromossomo da população
def adaptacao(adapt, pop):
  for i in range(len(pop)):
    adaptacao = 0
    for j in range(len(pop[i]) - 1):
      if pop[i][j] == 0 and pop[i][j + 1] == 1:
        adaptacao += 1
    adapt.append(adaptacao)

# mostra população com o valor de adaptação
def mostra_pop_adapt(adapt, pop):
  for i in range(10):
    print(adapt[i], " = ", pop[i])

# ordena a população com base no valor de adaptação de cada cromossomo, do maior valor ao menor
def ordena_pop(adapt, pop):
  for i in range(len(pop)):
    for j in range(len(pop)):
      if adapt[i] > adapt[j]:
        aux1 = adapt[i]
        adapt[i] = adapt[j]
        adapt[j] = aux1

        aux2 = pop[i]
        pop[i] = pop[j]
        pop[j] = aux2

# cruza cromossomos dado um ponto de corte aleatório
def cruzamento(pop, des):
  # pega apenas os 5 primeiros cromossomos da população para usar no cruzamento
  
  filho1 = []
  filho2 = []
  for i in range(5):
    for j in range(5):
      pai = pop[i]
      mae = pop[i + 1]
      x = rd.randint(1, 100)
      if x > 60 and len(des) <= 28:
        corte = rd.randint(1, 7)
        # adiciona os primeiro genes aos cromossomos filhos
        for k in range(corte):
          filho1.append(pai[k])
          filho2.append(mae[k])

        # adiciona os últimos genes aos cromossomos filhos
        for l in range(len(pai) - corte):
          filho1.append(mae[l + corte])
          filho2.append(pai[l + corte])

        des.append(filho1)
        des.append(filho2)
        filho1 = []
        filho2 = []


def mostra_des(des):
  for i in range(len(des)):
    print(des[i])

def mutacao(pop, des):
  for i in range(5):
    x = rd.randint(1, 100)
    if len(des) <= 29 and x > 90:
      for j in range(8):
        x = rd.randint(0, 2)
        if x == 0:
          if pop[i][j] == 0:
            des[i][j] = 1
          else:
            des[i][j] = 0

def inversao(pop, des):
  for i in range(5):
    x = rd.randint(1, 100)
    if x > 90 and len(des) <= 29:
      p1 = rd.randint(0, 7)
      p2 = rd.randint(0, 8)			
      for j in range(8):
        des.append(pop[i])	
      while p2 < p1:
        p2 = rd.randint(1, 8)					
      x = int((p2 - p1) / 2)
      if x == 0:
        x = 1
      for k in range(x):
        y = des[len(des)][p1 + k]
        des[len(des)][p1 + k] = des[len(des)][p2 - k]
        des[len(des)][p2 - k] = y

def inversao(pop, des):
  for a in range(5):
    x = rd.randint(1, 100)
    if x > 90 and len(des) <= 29:
      for b in range(8):
        des.append(pop[a][b])
      p1 = rd.randint(0, 7)
      p2 = rd.randint(0, 8)						
      while p2 < p1:
        p2 = rd.randint(0, 8)				
      x = int((p2-p1) / 2)
      for b in range(x):
        y = des[len(des)][p1 + b]
        des[len(des)][p1 + b] = des[len(des)][p2 - b]
        des[len(des)][p2 - b] = y

  
def adaptacaoD(adaptdes, des):
  for i in range(len(des)):
    for j in range(7):
      if des[j] == 0 and des[j + 1] == 1:
        adaptdes[i] = 1

def mostra_pop_adaptD(adaptdes, des):
  print(adaptdes)
  for i in range(len(des)):
    print(des[i])

def ordena_popD(adaptdes, des):
  for a in range(len(des) - 1):
    for b in range(len(des)):
      if adaptdes[a] < adaptdes[b]:							
        for i in range(8):
          c = des[a][i]
          des[a][i] = des[b][i]
          des[b][i] = c
        c = adaptdes[a]
        adaptdes[a] = adaptdes[b]
        adaptdes[b] = c

# também não sei o que tá rolando aqui nessa outra bosta
def substituicao(pop, des, adapt, adaptdes):
  b = 0
  c = 0
  pop_sub = pop
  adaptdes_sub = adaptdes
  for a in range(10):
    if b <= 10 and c <= len(des): 
      if adapt[b] > adaptdes[c]:
        for i in range(8):
          pop_sub[a][i] = pop[b][i]
        adaptdes_sub[a] = adapt[b]
        b = b + 1
      else:
        for i in range(8):
          pop_sub[a][i] = des[c][i]
        adaptdes_sub[a] = adaptdes[c]
        c = c + 1
						 
    else:
      if b <= 10 and c > len(des):
        for i in range(8):
          pop_sub[a][i] = pop[b][i]
        adaptdes_sub[a] = adapt[b]
        b = b + 1
      else:
        for i in range(8):
          pop_sub[a][i] = des[c][i]
        adaptdes_sub[a] = adaptdes[c]
        c = c + 1

  for a in range(10):
    for i in range(8):
      pop[a][i] = pop_sub[a][i]
    adapt[a] = adaptdes_sub[a]

pop = []
adapt = []
des = []
adaptdes= [0] * 30
aux = []

print("\n--- População atual gerada ---\n")
gera_pop_in(pop)
mostra_pop(pop)

print("\n--- População atual com sua adaptação ---\n")
adaptacao(adapt, pop)
mostra_pop_adapt(adapt, pop)

print("\n--- População atual na ordem do mais adaptável ao menos adaptável ---\n")
ordena_pop(adapt, pop)
mostra_pop_adapt(adapt, pop)

while range(len(adapt)) != 4:
  print("\n--- Cruzamento ---\n")
  cruzamento(pop, des)
  mostra_des(des)

  print("\n--- Mutação ---\n")
  mutacao(pop, des)
  mostra_des(des)

  print("\n--- Inversao ---\n")
  inversao(pop, des)
  mostra_des(des)

  print("\n--- População descencente com sua adaptação ---\n")
  adaptacaoD(adaptdes, des)
  mostra_pop_adaptD(adaptdes, des)

  print("\n--- População descendente na ordem decrescente da adaptação ---\n")
  ordena_popD(adaptdes, des)
  mostra_pop_adaptD(adaptdes, des)

  print("\n--- População nova ---\n")
  substituicao(pop, des, adapt, adaptdes)
  mostra_pop_adapt(adapt, pop)