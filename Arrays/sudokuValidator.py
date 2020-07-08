def sValidator(grid):

    for i in range(9): # validate the rows
        cache = {}
        for item in grid[i]:
            if item != '.' and item not in cache:
                cache[item] = 1

            ans = False
        ans  = True

    for j in range(9): # validate the columns
        print(grid[i][3])

        

if __name__ == "__main__":
    grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
    print(sValidator(grid))