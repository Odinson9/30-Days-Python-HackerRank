def factorial(N):
    N = int(N)
    if N == 1: # Base Case
        return 1
    else: # Recursive Case
        return N * factorial(N - 1) # Takes parameter and multiples by recursive function
    
print(factorial(int(input())))