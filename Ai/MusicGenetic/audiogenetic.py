from __future__ import print_function
import random
import time
import librosa
import math
import numpy as np


filename = "p.wav"
y, sr = librosa.load(filename)
f2 = "d.wav"
y2, sr2 = librosa.load(f2)

deviant = y2
dl = len(deviant)
#print("Enter Goal: ")
OPTIMAL = y.tolist()
DNA_SIZE = len(y)
#print("Enter Population size: ")
POP_SIZE = 3
#print("Enter Generation Size: ")
GENERATIONS = 1


def weighted_choice(items):
    """
    Chooses a random element from items, where items is a list of tuples in
    the form (item, weight). weight determines the probability of choosing its
    respective item. Note: this function is borrowed from ActiveState Recipes.
    """
    weight_total = sum((item[1] for item in items))
    n = random.uniform(0, weight_total)
    for item, weight in items:
        if n < weight:
            return item
        n = n - weight
    return item


def random_float():
    """
    Return a random character between ASCII 32 and 126 (i.e. spaces, symbols,
    letters, and digits). All characters returned will be nicely printable.
    """
    return float(math.cos(random.randrange(0, 3)))


def random_population():
    """
    Return a list of POP_SIZE individuals, each randomly generated via iterating
    DNA_SIZE times to generate a string of random characters with random_char().
    """
    pop = []
    for i in range(POP_SIZE):
        dna = []
        for c in range(DNA_SIZE):
            #if c%1000 == 0:
             #   dna.append(random_float())
            #elif c > int(DNA_SIZE-(DNA_SIZE/5)) and c < dl:
              #  dna.append(deviant[c])
            #else:
             #   dna.append(OPTIMAL[c])
            dna.append(float((OPTIMAL[c]+(random_float()/2))/2))
        pop.append(dna)
    return pop


#
# GA functions
# These make up the bulk of the actual GA algorithm.
#

def fitness(dna):
  """
  For each gene in the DNA, this function calculates the difference between
  it and the character in the same position in the OPTIMAL string. These values
  are summed and then returned.
  """
  fitness = 0
  for c in range(int(DNA_SIZE)):
    fitness += abs(dna[c] - OPTIMAL[c])
  return fitness

def mutate(dna):
  """
  For each gene in the DNA, there is a 1/mutation_chance chance that it will be
  switched out with a random character. This ensures diversity in the
  population, and ensures that is difficult to get stuck in local minima.
  """
  dna_out = []
  mutation_chance = 80
  for c in range(DNA_SIZE):
    if int(random.random()*mutation_chance) == 1 :
      dna_out.append(float(((random_float()/20)+OPTIMAL[c])/2))
    else:
      dna_out.append(dna[c])
  return dna_out

def crossover(dna1, dna2):
  """
  Slices both dna1 and dna2 into two parts at a random index within their
  length and merges them. Both keep their initial sublist up to the crossover
  index, but their ends are swapped.
  """
  pos = int(random.random()*DNA_SIZE)
  #child1 = dna1
  #child2 = dna2
  #for i in range(pos, DNA_SIZE):
      #child1[i] = dna2[i]
      #child2[i] = dna1[i]
  return (dna1[:pos] + dna2[pos:], dna2[:pos] + dna1[pos:])

  return (child1, child2)

#
# Main driver
# Generate a population and simulate GENERATIONS generations.
#

if __name__ == "__main__":
  print("Start.")
  # Generate initial population. This will create a list of POP_SIZE strings,
  # each initialized to a sequence of random characters.
  population = random_population()
  print("First Population Created.")
  # Simulate all of the generations.
  ftime = time.time()
  for generation in range(GENERATIONS):
    if generation == 0:
        ftime = time.time()
    else:
        elapsedtime = time.time() - ftime
        print("'%s' Time has passed" % int(elapsedtime))
    print( "Percent: '%s'" % (int((generation/GENERATIONS)*100)))
    weighted_population = []

    # Add individuals and their respective fitness levels to the weighted
    # population list. This will be used to pull out individuals via certain
    # probabilities during the selection phase. Then, reset the population list
    # so we can repopulate it after selection.
    for individual in population:
      fitness_val = fitness(individual)

      # Generate the (individual,fitness) pair, taking in account whether or
      # not we will accidently divide by zero.
      if fitness_val == 0:
        pair = (individual, 1.0)
      else:
        pair = (individual, 1.0/fitness_val)

      weighted_population.append(pair)

    population = []

    # Select two random individuals, based on their fitness probabilites, cross
    # their genes over at a random point, mutate them, and add them back to the
    # population for the next iteration.
    for _ in range(int(POP_SIZE/2)):
      # Selection
      ind1 = weighted_choice(weighted_population)
      ind2 = weighted_choice(weighted_population)

      # Crossover
      ind1, ind2 = crossover(ind1, ind2)

      # Mutate and add back into the population.
      population.append(mutate(ind1))
      population.append(mutate(ind2))

  # Display the highest-ranked string after all generations have been iterated
  # over. This will be the closest string to the OPTIMAL string, meaning it
  # will have the smallest fitness value. Finally, exit the program.
  fittest_string = population[0]
  minimum_fitness = fitness(population[0])

  for individual in population:
    ind_fitness = fitness(individual)
    if ind_fitness <= minimum_fitness:
      fittest_string = individual
      minimum_fitness = ind_fitness

  librosa.output.write_wav('fittest.wav', np.array(fittest_string), sr)
  print("Fittest Song Created.")
  #print ("Fittest song: %s" % fittest_string)
  exit(0)