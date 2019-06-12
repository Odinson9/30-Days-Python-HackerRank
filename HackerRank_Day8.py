def phone_book():
    number_of_people = int(input()) # takes initial input of number of entries
    phonebook = {} # dict placeholder
    for i in range(number_of_people): # iterates n number of times
        name, number = input().split(' ') # assigns name and number
        phonebook[name] = number # appends to dictionary
    while True: # infinite loop
        try:
            lookup = input() # asks for input if any
            if lookup in phonebook: # searches dictionary
                print('{0}={1}'.format(lookup,phonebook[lookup])) # if in dictionary, prints name and number
            else:
                print('Not found') # if not in dictionary, prints desired message
        except: # if no input is found, breaks the infinite loop
            break
        
phone_book()