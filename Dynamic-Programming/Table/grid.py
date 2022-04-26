# You are traveler on a 2D grid. You begin in the top left corner and your goal is to travel to the bottom -right  corner. You may only move down or right.

# In how many ways can you travel to the goal on a grid with dimensions m * n 
# Write a function gridTraveler(m, n) that calculates this...

def gridTraveler(m, n):
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j] 
            if (i+1) <= m:
                table[i+1][j] += current
            if (j+1) <= n:

                table[i][j+1] += current
               
          
    # print(m, n,"ending""")
    return table[m][n]


print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(3, 2))
print(gridTraveler(3, 3))
print(gridTraveler(18, 18))


# Time complexity is O(m*n) and space = O(m*n)