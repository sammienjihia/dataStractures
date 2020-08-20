class Permutation:
    def __init__(self):
        self.mySet = set()

    def swap(self, myString, left, index):
        # NB: String are imutable, meaning you'll have to change it to an array, perform the swap then change it back to a string
        stringAsList = list(myString)

        # swap the characters in the given indices
        stringAsList[left], stringAsList[index] = stringAsList[index], stringAsList[left]

        # reconvert list to string
        return ''.join(str(e) for e in stringAsList)

    def calculate(self, someString, left, right):
        
        # base case 
        if left == right: # this means the permutation of a single character shall always be 1
            print(self.mySet)
            return

        else:
            for i in range(len(someString)):
                # call swap method
                newString = self.swap(someString, left, i)

                # add string to set
                if newString not in self.mySet:
                    self.mySet.add(newString)

                # recursively perform the calculate function with the new permutation
                self.calculate(newString, left+1, right)

if __name__ == "__main__":
    x = Permutation()
    x.calculate("ABCD", 0, len("ABCD")-1)