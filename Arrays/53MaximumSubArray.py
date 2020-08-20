"""
This a typical dynamic problem
Using kadane's algorithm, we can compute the max sum of all elements until a given index by;
max sum at index i = max(max sum at index i-1 + element at index i, element at index i)

We already know that the max sum at index 0 is equal to the element at index 0
max sum at index 0 = nums[0]

max sum at index 1 = max(max sum at index 0 + nums[1], nums)

The global max sum at index i is the max of (max sum at index i, global max sum while at index n < i)

the global max at index 0 = nums[0]

the global max at index 1 = max of (max sum at index 1, global max at index 0)

"""

def solution(nums):
    # intialise the global max and the current max
    current_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        # get current max
        current_max = max(current_max+nums[i], nums[i])
        global_max = max(current_max, global_max)

    return global_max

if __name__ == "__main__":
    print(solution([-2,1,-3,4,-1,2,1,-5,4]))