"""
Given n items each with a weight and a value find the selection of the items that will return the maximum value if given a 
capacity to satisfy

Example 

n = 5
capacity = 10

Number of items
_____________________
| 1 | 2 | 4 | 2 | 5 | Weight
|___|___|___|___|___|
| 5 | 3 | 5 | 3 | 2 | Value
|___|___|___|___|___|

n = number of items left to consider
c = capacity left
v = value
"""

cache = {}
def ks(n, c):
    value = [0,5,3,5,3,2]
    wieght = [0,1,2,4,2,5]

    if (n,c) in cache:
        return cache[(n,c)]


    # base case
    if n == 0 or c == 0: # if the capacity left is 0 or there are 0 left items
        result = 0

    elif wieght[n] > c:
        result = ks(n-1, c)

    else:
        """
        If we decide to add an item to the knapsack, the the value in the knapsack shall be 
        the value of the current item in the list which is v(n) plust the value of the item to be added in the knapsack
        which essentially is ks(n-1, c-w[n]) where n-1 is the next item in the list, and c-w[n]
        is the reduction of our knapsack capacity by the weight of the current item in the list

        value_of_ks_if_added_2_items = value_of_ks_if_added_1_items + value_of_ks_if_added_1_items
        """
        yes = value[n] + ks(n-1, c-wieght[n]) # if we add it then we call ks with the next item and a reduced capacity with the current item
        no = ks(n-1, c) # if we don't add it we just move to the next item, capacity doesn't change

        result = max(yes, no)
        cache[(n,c)] = result
        print("result {}".format(result))

    return result

if __name__ == "__main__":
    ks(5,10)