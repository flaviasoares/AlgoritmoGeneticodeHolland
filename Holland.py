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
  adaptacao = 0
  for i in range(8):
    for j in range(7):
      if pop[i][j] == 0 and pop[i][j + 1] == 1:
        adaptacao += 1
    adapt.append(adaptacao)
    adaptacao = 0

# mostra população com o valor de adaptação
def mostra_pop_adapt(adapt, pop):
  for i in range(8):
    print(adapt[i], " = ", pop[i])

# ordena a população com base no valor de adaptação de cada cromossomo
def ordena_pop(adapt, pop):
  for i in range(8):
    for j in range(7):
      if adapt[i] > adapt[j]:
        aux1 = adapt[i]
        adapt[i] = adapt[j]
        adapt[j] = aux1

        aux2 = pop[i]
        pop[i] = pop[j]
        pop[j] = aux2

# cruza cromossomos dado um ponto de corte aleatório
def cruzamento(pop, des):
  # pega apenas os 5 ultimos cromossomos da população para usar no cruzamento
  filho1 = []
  filho2 = []
  for i in range(5):
    for j in range(5):
      x = rd.randint(1, 100)
      if x > 60 and len(des) <= 28:
        corte = rd.randint(1, 7)
        pai = pop[len(pop[i]) - i]
        mae = pop[len(pop[j]) - j]
        if i != j:
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

def mutacao(pop, des):
  for i in range(5):
    x = rd.randint(1, 100)
    if len(des) <= 29 and x > 90:
      for j in range(8):
        x = rd.randint(0, 1)
        if x == 0:
          if pop[i][j] == 0:
            des[i][j] = 1
          else:
            des[i][j] = 0
        else:
            des[len(des) - 1][j] = pop[i][j]

def inversao(pop, des):
  for a in range(5):
    x = rd.randint(0, 100)
    if x > 90 and (len(des) - 1) <= 29:
      des.append(pop[a])

      p1 = rd.randint(0, 7)
      p2 = rd.randint(0, 8)	

      while p2 < p1:
        p2 = rd.randint(0, 8)					
      
      x = int((p2 - p1) / 2)
					
      for b in range(x):
        aux = des[len(des) - 1][p1 + b]
        des[len(des) - 1][p1 + b] = des[len(des) - 1][p2 - b]
        des[len(des) - 1][p2 - b] = aux
          

pop = []
adapt = []
des = []
adaptDes= []
aux = []

print("\n--- População atual gerada ---\n")
gera_pop_in(pop)
mostra_pop(pop)

print("\n--- População atual com sua adaptação ---\n")
adaptacao(adapt, pop)
mostra_pop_adapt(adapt, pop)

print("\n--- População atual na ordem decrescente da adaptação ---\n")
ordena_pop(adapt, pop)
mostra_pop_adapt(adapt, pop)

while adapt[len(adapt) - 1] != 4:
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
  mostra_pop_adapt(adapt, pop)
