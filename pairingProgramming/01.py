# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# jewels = "aA"

# stones = "aAAbbbb"

# counter = 0

# for x in stones:
#   for y in jewels:
#     if(x == y):
#       counter = counter + 1

# print(counter)

# # function that filters vowels 
# def fun(variable): 
#     letters = ['a', 'A', 'A', 'b', 'b'] 
#     if (variable in letters): 
#         return True
#     else: 
#         return False

# print(fun(['A','a']))

# 'aA' in stones

# print('aA' in stones)

# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"

letters = "codeleet"
indices = [4,5,6,7,0,2,1,3]

# Return double of n 
def addition(index, letter): 
    return (index, letter)

numbers = (1, 2, 3, 4) 
result = list(map(addition, indices, letters)) 
print(result.sort())
