# Class PopulationSpace:
# Handles individuals, crossover, and mutation.
import random
from utils.graph_generator import GraphGenerator
from typing import TYPE_CHECKING, List
from algorithms.cultural.individual import Individual


class PopulationSpace:
    def __init__(self, pop_size, path, random_selection=0, focused_mutation=0):
        self.random_graph = GraphGenerator(path)
        self.pop_size = pop_size
        self.n_nodes = self.random_graph.n_nodes
        self.random_selection = random_selection  # 0 = tournament, 1 = random
        self.focused_mutation = focused_mutation  # 0 = normal mutation, 1 = focused mutation
        
    def create_chromosome(self, max_colors):
        chromosome = [random.randint(1, max_colors) for _ in range(self.n_nodes)]
        return chromosome

    def initialize_population(self, max_colors):
        pop = [Individual(self.create_chromosome(max_colors)) for _ in range(self.pop_size)]
        return pop
    
    def evaluate_and_get_best(self, population):
        for ind in population:
            self.calculate_fitness(ind)
        return min(population, key=lambda x: x.fitness)

    def calculate_fitness(self, individual: 'Individual'):
        chromo = individual.chromosome
        bad_edges = 0
        
        for u, adj in self.random_graph.graph.items():
            u_color = chromo[u-1]

            for v in adj:
                #condition to check adjacany once
                if(v >= u):
                    v_color = chromo[v-1]  
                    if u_color == v_color:
                        bad_edges += 1
        
        individual.fitness = bad_edges
        return bad_edges
    
    def run_estimation_phase(self):
        initial_pop: List['Individual'] = self.initialize_population(self.n_nodes)

        for ind in initial_pop:
            self.calculate_fitness(ind)
        
        best_ep_individual = min(initial_pop, key=lambda x: x.belief)
        return best_ep_individual.belief, initial_pop


    def selection(self, population: List['Individual']):
        parent_one = min(random.sample(population, 2), key=lambda x: x.fitness)
        parent_two = min(random.sample(population, 2), key=lambda x: x.fitness)
        return parent_one, parent_two
    

    def selection_random(self, population: List['Individual']):
        parent_one = random.choice(population)
        parent_two = random.choice(population)
        return parent_one, parent_two
    

    def crossover(self, parent_one : 'Individual', parent_two : 'Individual'):
        n = len(parent_one.chromosome)
        crosspoint = random.randint(0, n-2)
        child = parent_one.chromosome[:crosspoint+1] + parent_two.chromosome[crosspoint + 1:]
        # print(crosspoint)
        # print(self.calculate_fitness(parent_one))
        # print(self.calculate_fitness(parent_two))
        # print(self.calculate_fitness(child))
        
        child_ind = Individual(child)
        return child_ind

    def mutation(self,child_individual : 'Individual', general_belief):            
            chromo = child_individual.chromosome
            available_colors = list(range(1,general_belief+1))  #influence the population space by constraining the range of colors
            vertex_index = random.randint(0, self.n_nodes - 1)
            chromo[vertex_index] = random.choice(available_colors)

            return child_individual
    
    def apply_focused_mutation(self,child_individual : 'Individual', general_belief):
        chromo = child_individual.chromosome

        conflicted_nodes_indices = set()
        for u, adj in self.random_graph.graph.items():
            u_color = chromo[u - 1]
            for v in adj:
                if v > u and u_color == chromo[v-1]:
                    conflicted_nodes_indices.add(u - 1)
                    conflicted_nodes_indices.add(v - 1)

        if not conflicted_nodes_indices:
            return self.mutation(child_individual, general_belief)
        
        node_index_to_mutate = random.choice(list(conflicted_nodes_indices))
        available_colors = list(range(1, general_belief + 1))

        chromo[node_index_to_mutate] = random.choice(available_colors)

    def perform_variation(self, population, pop_size, general_belief, muation_rate):
        new_pop = []
        num_children_to_generate = pop_size

        for _ in range(num_children_to_generate):
            # Choose selection method based on random_selection parameter
            if self.random_selection == 1:
                p1, p2 = self.selection_random(population)
            else:
                p1, p2 = self.selection(population)
            
            child = self.crossover(p1,p2)

            if random.random() < muation_rate:
                # Choose mutation method based on focused_mutation parameter
                if self.focused_mutation == 1:
                    self.apply_focused_mutation(child, general_belief)
                else:
                    self.mutation(child, general_belief)
            
            self.calculate_fitness(child)
            new_pop.append(child)
        return new_pop
            
            
#70 = 70
