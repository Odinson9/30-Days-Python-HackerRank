def bubble_sort():
    '''Runs in O(n^2) time.'''
    n = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    numSwaps = 0 # tracks number of swaps
    for j in range(n): # for each index
        for i in range(1, n): # runs n-1 seperate checks
            if a[i] < a[i-1]: # if the left number is greater than the right number
                a[i-1], a[i] = a[i], a[i-1] # transpose action
                numSwaps += 1 # counts a swap
            else:
                None
    print('Array is sorted in {0} swaps.'.format(numSwaps))        
    print('First Element: {0}'.format(a[0]))
    print('Last Element: {0}'.format(a[-1]))

bubble_sort()