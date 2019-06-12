def string_to_int():
    S = input().strip() # takes input
    try: # try block
        print(int(S)) # prints string if it can be converted to an int
    except: # error/except block
        print('Bad String') # error message

string_to_int()