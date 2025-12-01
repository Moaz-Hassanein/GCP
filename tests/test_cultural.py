import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from algorithms.cultural.population_space import PopulationSpace
from typing import TYPE_CHECKING, List


graph_path = project_root / "data" / "sample_graphs" / "graph_two"

saved_population = None

def test_pop_space_operators():
    global saved_population

    pop_size = 10
    ps = PopulationSpace(pop_size, graph_path)

    if saved_population is None:
        print("Initializing new population...")
        saved_population = ps.initialize_population(ps.n_nodes)
        ps.evaluate_and_get_best(saved_population)
    else:
        print("Reusing existing population...")

    print(f"Initial Population (Size {len(saved_population)}):")
    for i in range(pop_size):
        print(f"  {saved_population[i].chromosome} -> {saved_population[i].fitness}")

    p1, p2 = ps.selection(saved_population)
    print(f"\nSelected Parents (by lowest fitness):")
    print(f"  Parent 1: {p1.chromosome} -> {p1.fitness}")
    print(f"  Parent 2: {p2.chromosome} -> {p2.fitness}")
    assert p1.fitness is not None and p2.fitness is not None, "Parents must have calculated fitness."




test_pop_space_operators()
print("\n" + "="*50)
print("Running test again with same population:")
print("="*50)
test_pop_space_operators()
print("\n" + "="*50)
print("Running test again with same population:")
print("="*50)
test_pop_space_operators()
print("\n" + "="*50)
print("Running test again with same population:")
print("="*50)
test_pop_space_operators()