def array_reverse1():
    n = int(input().strip())
    arr = [str(arr_temp) for arr_temp in input().strip().split(' ')] # changed int variable to str an created a list
    print(' '.join(arr[::-1])) # joins list in reverse and inserts a space after each number
    
array_reverse1()