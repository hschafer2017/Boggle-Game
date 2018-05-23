# l = [1,3,5]

# # p = []
# # for n in l: 
# #         p.append(n*2)

# p = [n*2 for n in l]

# print(p)


# # [0,2,4,6,8,10,12]

# print([i % 2 == 0 for i in range(0,7)])

# print([ i == j for i in range(0,10) for j in range(0,10)])

# print([ [ j for j in range(i)] for i in range(0,10) for j in range(0,10)])

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