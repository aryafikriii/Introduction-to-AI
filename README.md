# Genetic Algorithm for Function Optimization

This project focuses on the analysis, design, and implementation of a Genetic Algorithm (GA) to find the minimum value of a given function ℎ(𝑥, 𝑦). The goal is to search for the optimal values of 𝑥 and 𝑦 within the specified domain to minimize the function.

## Function Definition

The function to be minimized is defined as follows:

ℎ(𝑥, 𝑦) = (cos 𝑥 + sin 𝑦)^2 / (𝑥^2 + 𝑦^2)

The domain (bounds) for 𝑥 and 𝑦 is:
−5 ≤ 𝑥 ≤ 5 and −5 ≤ 𝑦 ≤ 5

## Genetic Algorithm Design

To solve the optimization problem, the following aspects need to be analyzed and designed:

1. Chromosome Design and Decoding Method: Determine the representation of the individuals in the population and devise a decoding method to translate the chromosome into meaningful values of 𝑥 and 𝑦 within the given domain.

2. Population Size: Determine the size of the population, i.e., the number of individuals in each generation.

3. Parent Selection Method: Choose a method for selecting parents from the population to participate in reproduction.

4. Genetic Operators: Define the genetic operators, such as crossover (recombination) and mutation, to create new offspring from the selected parents.

5. Genetic Operator Probabilities (𝑃𝑐 and 𝑃𝑚): Set the probabilities for applying the genetic operators during reproduction.

6. Generation Replacement Method (Survivor Selection): Determine how to select individuals from the current population and the newly created offspring for the next generation.

7. Termination Criteria: Define the criteria to stop the evolution process, such as reaching a certain number of generations or achieving a satisfactory fitness level.

## Implementation

The following steps already implemented in the program:

1. Chromosome Decoding: Implement a method to decode the chromosome representation and obtain meaningful values of 𝑥 and 𝑦 within the specified domain.

2. Fitness Calculation: Evaluate the fitness of each individual in the population based on the defined function ℎ(𝑥, 𝑦).

3. Parent Selection: Select parents from the population for reproduction based on the chosen parent selection method.

4. Crossover (Recombination): Apply crossover (recombination) to create new offspring from the selected parents.

5. Mutation: Apply mutation to introduce small changes in the offspring's chromosomes.

6. Generation Replacement: Select individuals for the next generation based on the survivor selection method.

## Output

The program provide the following output:

1. Best Chromosome: The chromosome that represents the individual with the highest fitness in the final generation.

2. Decoded 𝑥 and 𝑦 Values: The decoded values of 𝑥 and 𝑦 obtained from the best chromosome.

These outputs will indicate the best solution found by the genetic algorithm, providing the 𝑥 and 𝑦 values that yield the minimum value of the defined function ℎ(𝑥, 𝑦).

## Contact

If you have any questions or suggestions regarding this project, please feel free to contact me. You can reach me at [aryafikriansyah@gmail.com].
