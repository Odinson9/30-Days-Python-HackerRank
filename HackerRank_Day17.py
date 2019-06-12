class Calculator(object):
    def power(self, n, p): # method
        if n < 0 or p < 0: # exception cases
            raise Exception('n and p should be non-negative') # Error message
        else:
            exponential = n ** p # exponential function
            return exponential 
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)  