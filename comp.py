# List Comprehension Challenges
# Example:
# Question 
#                 range(10) 
#                 -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Answer
#                 [n * 2 for i in range(10)]
# 1. range(5) 
# -> ["*", "*", "*", "*", "*"]

print([ "*" for i in range(5)])

# 2. ["Hi", "There", "Everyone"] 
# -> [2, 5, 8]
greet = ["Hi", "There", "Everyone"]
print([len(i) for i in greet])

# 3. range(8) 
# [0, 1, 4, 9, 16, 25, 36, 49]
print([i**2 for i in range(8)])

# 4. range(5) 
# -> [(0,1), (1,2), (2,3), (3,4), (4,5)]
print([(i,i+1) for i in range(5)])

# 5. 'woohoo' 
woohoo = ['w', 'o', 'o', 'h', 'o', 'o']
print([i for i in woohoo])

stuff = ['car', 'cat', 'maps', 'if', 'level'] 
# -> [('car', 3), ('cat', 3), ('maps', 4), ('if', 2), ('level', 5)]
print([(i, len(i)) for i in stuff])


bools = [(False, False), (False, True), (True, False), (True, True)]
# ->[False, False, False, True]
print([(i and j) for i,j in bools])

boolz = [(False, False), (False, True), (True, False), (True, True)]
# ->[False, True, True, True]
print([(i or j) for i,j in boolz])