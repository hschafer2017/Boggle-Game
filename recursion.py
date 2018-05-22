# Finding the sum of a list using recursion 
def sum(l): 
    if len(l) == 0: 
        return 0 
    else: 
        return l[0] + sum(l[1:]) 

print(sum([12,42,13]))

# Finding the maximum value in a list using recursion 
def max_val(n):
    if len(n) == 1:
        return n[0]
    else: 
        m = max_val(n[1:])
        return m if m > n[0] else n[0]
    
print(max_val([2,5,-13,7,8]))

# Finding the minimum value in a list using recursion 
def min_val(n):
    if len(n) == 1:
        return n[0]
    else: 
        m = min_val(n[1:])
        return m if m < n[0] else n[0]
    
print(min_val([2,5,-13,7,8]))