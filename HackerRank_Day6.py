def mixed_word(word):
    even_word = word[::2] # appends every 2 indicies starting at index 0
    odd_word = word[1::2] # appends every 2 inidicies starting at index 1
    return'{0} {1}'.format(even_word, odd_word) # joins individual word structures and then prints in correct format

def full_input():
    for i in range(int(input().strip())): # creates number of iterations based on input
        print(mixed_word(input().strip())) # calls mixed_words for each input and then prints
        
full_input()