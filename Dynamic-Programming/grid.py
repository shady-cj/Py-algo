# You are traveler on a 2D grid. You begin in the top left corner and your goal is to travel to the bottom -right  corner. You may only move down or right.

# In how many ways can you travel to the goal on a grid with dimensions m * n 

def grid(r, c):
    if r==1 and c ==1:
        return 1
    elif r==0 or c == 0:
        return 0
    else:
        return grid(r-1, c) + grid(r, c-1)

# print(grid(18,18))

# memoized version

def grid_memo(r, c, memo={}):
    idx = (r, c)
    if idx in memo:
        return memo[idx]
    elif r==1 and c==1:
        return 1
    elif r==0 or c== 0:
        return 0
    memo[idx] = grid_memo(r-1, c, memo) + grid_memo(r, c-1, memo)
    return memo[idx]

print(grid_memo(18,180))