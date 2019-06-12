class Person:
    def __init__(self, age):
        # Add some more code to run some checks on initialAge
        self.age = age
        self.initialAge = 0
        if self.age < 0:
            self.age = self.initialAge
            print('Age is not valid, setting age to 0.')
        else:
            self.initialAge = self.age
    
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')       
   
    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1