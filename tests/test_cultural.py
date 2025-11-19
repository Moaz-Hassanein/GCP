from algorithms.cultural import population_space
from utils.graph_generator import GraphGenerator
from algorithms.cultural.population_space import PopulationSpace


popInitialize = PopulationSpace(30)
N_NODES = popInitialize.random_graph.n_nodes
print(N_NODES)


test_chrmsm = popInitialize.create_chromosome(N_NODES)

test_pop = popInitialize.initialize_population()


test_fitness = popInitialize.calculate_fitness(test_chrmsm)


p1, p2 = popInitialize.selection(test_pop)

test_child=popInitialize.crossover(p1,p2)

test_allColors=[1,2,3,4,5]
popInitialize.mutation(test_child,test_allColors)
