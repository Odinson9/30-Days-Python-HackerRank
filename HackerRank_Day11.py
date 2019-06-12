def hourglass():
    arr = [] # array placeholder 
    result = []
    for arr_i in range(6): # given values
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')] # given values
        arr.append(arr_t) # given array

    for x in range(0, 4): # range for row of 16 hourglasses
        for y in range(0, 4): # range for column of 16 houglasses
            s = (arr[x][y] + arr[x][y+1] + arr[x][y+2] # 1st row of hourglass structure
                    + arr[x+1][y+1] # 2nd row of hourglass
                    + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]) # 3rd row of hourglass
            result.append(s) # appends sum to list
    
    print(max(result)) # prints max value
    
hourglass()