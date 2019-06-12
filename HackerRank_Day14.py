class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0 # instance variable set intially at 0
    def computeDifference(self): # difference method
        sorted_array = sorted(self.__elements) # sorts array
        self.maximumDifference = abs(sorted_array[0] - sorted_array[len(sorted_array) - 1]) # finds absolute difference
        return self.maximumDifference # returns absolute difference assigned in maximumDifference
# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)