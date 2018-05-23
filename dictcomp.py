# Dictionary Comprehension Challenges
# Example:
# Question 
#                 range(5) 
#                 -> { 0: "", 1:"*", 2:"**", 3:"***", 4:"****" }
# Answer
#                 { i:"*" * i for i in range(5)}
                
greet = ['Hi', 'There', 'Everyone'] 
# -> {'Hi':2, 'There':5, 'Everyone':8}
print({i: len(i) for i in greet})

# 2. 'code'
# -> {'c': 99, 'e': 101, 'd': 100, 'o': 111}


# 3. ['car', 'pop', 'maps', 'if', 'level'] 
# -> {'car':False, 'pop':True, 'maps':False, 'if':False, 'level':True}
