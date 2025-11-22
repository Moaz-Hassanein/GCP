class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome  #the color array for example - [2,1,3,4]
        self.fitness = 0   #number of conflicts (bad edges)
        self.belief = len(set(chromosome))  #beleif of the individual (best unique number of colors for the chromosome)

    def __lt__(self, other):  #used to find individual with better fitness by comparing it with other individual
        return self.fitness < other.fitness 
    
    