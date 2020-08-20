# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13

# function to return the nth fibonacci number

# nth = (n-1) + (n-2)

# x = [0,1]
# x[len(n)] + x[len(x)-1]


# using an array
# space complexity is O(n)
# time complexity is O(n)
def fibonacci(k):

    seq = [0,1]

    for x in range(0, k):
        seq.append(seq[x] + seq[x+1])

    return seq[k]

print(fibonacci(7))


# Using recursion
# Space complexity is O(1)
# time complexity is O(n**2)
def fib1(k):
    if k ==0 :
        return 0
    elif k == 1 or k == 2:
        return 1
    else:
        return fib(k-1) + fib(k-2)

# using a memoized solution
fib_cache = {}
def fib(n):

    if n in fib_cache:
        return fib_cache[n]

    # base case for our recurssive function
    if n==1 or n==2:
        return 1

    else:
        result = fib(n-1) + fib(n-2)

    fib_cache[n] = result 
    return result
# k=3
# output = 1

# [0, 1, 1, 2, 3]

# 1st iteration x= 0
# value in index 0 + value in index 1 = 0+1 = 1

# 2nd iteration x= 1
# value index 1 + value index 2 = 1 + 1 = 2

# 3rd iteration x=2
# value index 2 + value index 3 = 1+2 = 3

print(fib(7))








