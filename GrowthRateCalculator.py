import sympy as sp

# Growth rate calculator
# Change code below with functions you want and it will order them
# from least to greatest

# Symbol for n
n = sp.symbols('n')

# The functions (change for different problems)
functions = [
    ("n!", sp.factorial(n)), # n!
    ("1000^10", 1000**10), # 1000^10
    ("log_2(n)", sp.log(n, 2)), # log_2(n)
    ("2^n", 2**n), # 2^n
    ("(log_2(n))^n", sp.log(n, 2)**n), # (log_2(n))^n
    ("log_10(n^10)", sp.log(n, 10)**10), # log_10(n^10)
    ("(log_2(n))^10", sp.log(n, 2)**10), # (log_2(n))^10
    ("sqrt(n)", sp.sqrt(n)), # sqrt(n)
    ("5^(n/2)", 5**(n/2)) # 5^(n/2)
]

# Function to compare two functions using L'Hopital's rule
def lHopitalsRule(f1, f2):
    # the limit of f1 / f2 as n -> infinity
    limit = sp.limit(f1 / f2, n, sp.oo)
    
    if limit == sp.oo:
        return 1  # f1 grows faster than f2
    elif limit == 0:
        return -1  # f2 grows faster than f1
    else:
        return 0  # f1 and f2 grow at the same rate

# Sort functions based on L'Hopital's Rule
def orderFunctions(functions):
    n = len(functions)
    
    # Bubble sort!
    for i in range(n): # go through all functions
        for j in range(0, n-i-1): # the last should be the biggest already!
            if lHopitalsRule(functions[j][1], functions[j+1][1]) == 1:
                # bigger ones later
                functions[j], functions[j+1] = functions[j+1], functions[j]
    
    return functions

# Order the functions
ordered_functions = orderFunctions(functions)

# Display the now ordered functions
print("In order from least to greatest:")
for func in ordered_functions:
    print(func[0])
