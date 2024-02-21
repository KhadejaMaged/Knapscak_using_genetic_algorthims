import random

population_size = 50
mutation_rate = 0.01
generations = 100


def initialize_population():
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(len(w1))]
        population.append(chromosome)
    return population


def fitness_func(chromosome):
    total_w = 0
    total_val = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_w += w1[i]
            total_val += v1[i]
    if total_w > capacity:
        total_val = 0
    return total_val


def All_fitness_pop(pop):
    fitntess_val = []
    for i in range(len(pop)):
        fitntess_val.append(fitness_func(pop[i]))
    return fitntess_val


def rank_selection(population, fitness_val, num_selections):
    population_size = len(population)
    sorted_population = [x for _, x in sorted(zip(fitness_val, population), reverse=True)]
    selection_probs = []

    # Calculate selection probabilities
    for rank in range(1, population_size + 1):
        probability = 1.0 - (rank - 1) / (population_size - 1)
        selection_probs.append(probability)

    selected = []

    # Perform selection
    for _ in range(num_selections):
        rand_num = random.randint(0, 1)
        cumulative_prob = 0.0
        for i in range(population_size):
            cumulative_prob += selection_probs[i]
            if rand_num <= cumulative_prob:
                selected.append(sorted_population[i])
                break

    return selected


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(w1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def muatation(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.uniform(0, 1) <= mutation_rate:
            chromosome[i] = 1 - chromosome[i]

    return chromosome


def Replacement(population, parents, offspring):
    for i in range(len(population)):
        if population[i] == parents[0]:
            population[i] = offspring[0]

        elif population[i] == parents[1]:
            population[i] = offspring[1]

    return population


#########################################new main ###############################################################

file_path = 'knapsack_input.txt'
file = open(file_path, 'r')

lines = file.readlines()

# class test:
#
#     def __init__(self,size,numItems,weight,value):
#         self.size=size
#         self.numItems=numItems
#         self.weight=weight
#         self.value=value


ntestcase = int(lines[0])

j = 3

capacity = ntestcase

for i in range(0, ntestcase):

    sizeknapsack = int(lines[j])
    numItem = int(lines[j + 1])
    w1 = []
    v1 = []

    j += 2

    for k in range(0, numItem):
        k = j

        list = lines[k].strip().split()

        w1.append(int(list[0]))
        v1.append(int(list[1]))
        j += 1

    ########CALL###########################
    print(f"THE TEST CASE : {i + 1}")
    population = initialize_population()
    for i in range(generations):
        # print(f" number of iteration {i}")
        new_population = []
        list_off = []
        list_parent = []
        listf = All_fitness_pop(population)
        for j in range(int(population_size / 2)):
            # print(f" number of iteration {j}")
            c = random.randint(2, 10)
            parents = rank_selection(population, listf, c)
            offspring1, offspring2 = crossover(parents[0], parents[1])
            offspring1 = muatation(offspring1, 0.01)
            offspring2 = muatation(offspring2, 0.01)
        list_off = [offspring1, offspring2]
        new_population = Replacement(population, parents, list_off)
        population = new_population
    best_chromosome = max(population, key=lambda chromosome: fitness_func(chromosome))
    best_fitness = fitness_func(best_chromosome)
    print(f" the bests fitness of chromsosme {best_fitness}")
    c = 0
    count_val = 0
    count_weight = 0
    for i in range(len(best_chromosome)):
        if (best_chromosome[i] == 1):
            count_val += v1[i]
            count_weight += w1[i]
            c += 1

    print(f"The Number of selected Item =  {c} , The Total Values =  {count_val}, The total weight =  {count_weight}")

    for i in range(len(best_chromosome)):
        if (best_chromosome[i] == 1):
            print(f"The Value for each item  = :  {v1[i]} , The Weight for each item =  {w1[i]}")

    j = k + 3

