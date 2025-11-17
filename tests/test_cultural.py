from algorithms.cultural import population_space
from utils.graph_generator import GraphGenerator


N_NODES = population_space.random_graph.n_nodes
print(N_NODES)
population_space.random_graph.show()

test_chrmsm = population_space.create_chromosome(N_NODES)
# print(test_chrmsm)

test_pop = population_space.initialize_population(10)

test_fitness = population_space.calculate_fitness(test_chrmsm)
# print(test_chrmsm)
# print(test_fitness)

population_space.selection(test_pop)
p1, p2 = population_space.selection(test_pop)
print(f'p1 {p1}, p2 {p2}')


x = population_space.crossover(p1, p2)
print(x)

# 4 4    4 4   4 4  4 4   4  4