def wacky_number():
    N = int(input().strip())
    if N % 2 == 0: # checks even condition
        if N in list(range(2, 6)): # first condition
            print('Not Weird')
        elif N in list(range(6, 21)): # second condition
            print('Weird')
        else:
            print('Not Weird') # greater than 20
    else:
        print('Weird') # odd number
        
wacky_number()
