import random

# Define o tamanho da população
population_size = 10

# Define o tamanho do cromossomo
chromosome_size = 8

# Define o número máximo de gerações
max_generations = 100

# Define a taxa de crossover
crossover_rate = 0.8

# Define a taxa de mutação
mutation_rate = 0.1

# Função que retorna a quantidade de sequências "01" em um cromossomo
def count_01(chromosome):
    count = 0
    for i in range(len(chromosome)-1):
        if chromosome[i] == 0 and chromosome[i+1] == 1:
            count += 1
    return count

# Função que gera um cromossomo aleatório
def generate_chromosome():
    chromosome = []
    for i in range(chromosome_size):
        chromosome.append(random.randint(0, 1))
    return chromosome

# Função que gera uma população aleatória
def generate_population():
    population = []
    for i in range(population_size):
        population.append(generate_chromosome())
    return population

# Função que realiza o crossover entre dois cromossomos
def crossover(parent1, parent2):
    child1 = []
    child2 = []
    for i in range(chromosome_size):
        if random.random() < crossover_rate:
            child1.append(parent2[i])
            child2.append(parent1[i])
        else:
            child1.append(parent1[i])
            child2.append(parent2[i])
    return child1, child2

# Função que realiza a mutação em um cromossomo
def mutation(chromosome):
    for i in range(chromosome_size):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]

# Função que seleciona dois pais para o crossover
def selection(population):
    parents = random.sample(population, 2)
    return parents[0], parents[1]

# Função que realiza a evolução da população
def evolve(population):
    new_population = []
    for i in range(population_size):
        parent1, parent2 = selection(population)
        child1, child2 = crossover(parent1, parent2)
        mutation(child1)
        mutation(child2)
        new_population.append(child1)
        new_population.append(child2)
    return new_population

# Função que retorna o cromossomo mais adaptado da população
def get_best_chromosome(population):
    best_chromosome = population[0]
    best_fitness = count_01(best_chromosome)
    for chromosome in population:
        fitness = count_01(chromosome)
        if fitness > best_fitness:
            best_chromosome = chromosome
            best_fitness = fitness
    return best_chromosome, best_fitness

# Gera a população inicial
population = generate_population()

# Roda o algoritmo evolucionário
for generation in range(max_generations):
    population = evolve(population)
    best_chromosome, best_fitness = get_best_chromosome(population)
    print(f"Generation {generation+1}: Best fitness = {best_fitness}")
    
print(f"Best chromosome: {best_chromosome}")
