def binary(n):
    binary_string = '' # binary placeholder
    while n >= 1: 
        remainder = n % 2 # looks for remainder of a base-10 number divided by base 2
        binary_string += str(remainder) # adds remainder i.e, 0 or 1 to binary string
        n = n // 2 # decreases number by factor of 2 ignoring the remainder
    return int(binary_string[-1::-1]) # returns binary string backwards, to match binary structure

def longest_consec_1():
    n = int(input().strip()) # input value
    bin_number = str(binary(n)) # stores the binary of a number in a var
    ones_list = bin_number.split('0') # splits binary by placement of zeros
    print(len(max(ones_list))) # finds max number of list of 1s and returns length
    
longest_consec_1()