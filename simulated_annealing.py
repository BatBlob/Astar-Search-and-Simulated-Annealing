import math, random
from operator import truediv
import decimal




# def calc_func(coefficients, current_vars) -> float:
#     result = 0
    
#     for var in range(len(coefficients)-1):
#         for coeff in range(len(coefficients[var])):
#             result += (coefficients[var][coeff] * (current_vars[var] ** (coeff + 1)))

#     return result + coefficients[-1]

def choose_random_neighbour(current_vars, limits, step):
    equal = True

    while equal:
        neighbours = []

        for var in range(len(current_vars)):
            possible_changes = [-step, 0, step]

            for change in [possible_changes[0], possible_changes[-1]]:
                if ((current_vars[var] + change) < limits[var][0]) or ((current_vars[var] + change) > limits[var][1]):
                    possible_changes.remove(change)

            neighbours.append(current_vars[var] + (random.choice(possible_changes)))
        
        if neighbours != current_vars:
            equal = False
    
    return neighbours

def compare(n1, n2):
    if maximum:
        return n1 > n2
        
    return n1 < n2

def simulated_annealing(limits: list[list[float, float],], dimensions: int, maximum: bool, step: float, func) -> None:
    
    current_vars = [ random.randint(low, up) for low, up in limits ]

    # current_out = calc_func(coefficients, current_vars)
    current_out = func(*current_vars)

    if step == 0:
        step = 1

    temperature = current_out * (1 - factor)

    for _ in range(200):
        for _ in range(Iterations):
            trial = choose_random_neighbour(current_vars, limits, step)
            # trial_out = calc_func(coefficients, trial)
            trial_out = func(*trial)
            
            delta = trial_out - current_out
            if delta > 0:
                current_out = trial_out
                current_vars = trial[:]
            
            else:
                # if compare(math.exp(delta / temperature), random.random()):
                if compare(math.exp(delta / temperature), random.random()):
                    current_out = trial_out
                    current_vars = trial[:]

        temperature *= factor
        
    return current_out, current_vars

def Sphere(x, y):
    return (x**2 + y**2)

def Rosenbrock(x, y):
    return (100 * (x**2 - y)**2) + ((1 - x)**2)

def Griewank(x, y):
    return ((x**2+y**2)/4000) - (math.cos(x) * math.cos(y / math.sqrt(2))) + 1


Iterations: int = 100
factor: float = 0.8
dimensions: int = 3
maximum: bool = True
step: float = 0.1
func = Griewank
# equation: str = "x**2 + y**2"

'''Coefficients of variables with each nested list containing elements equal to
   the polynomial degree of the function for each variable. Last nested list
    should contain one element only, i.e the constant'''
# coefficients: list[float] = [[0, 1], [0, 1], 0]
# coefficients = [[-100, 0], [101, -2], 1]

'''Lower and upper limit of each variable, parallel to the mathematical functions' arguments'''
limits: list[list[int, int],] = [[-5, 5], [-5, 5]]
# limits = [[-1, 3], [-2, 2]]


out, out_vars = simulated_annealing(limits, dimensions, maximum, step, func)
print(out, out_vars)
# print(eval(equation))
