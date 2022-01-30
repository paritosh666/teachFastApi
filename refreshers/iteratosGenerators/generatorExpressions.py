'''
generator expressions as a high performance, memory efficient generalization of list comprehensions


Experience with list comprehensions has shown their widespread utility throughout Python. 
However, many of the use cases do not need to have a full list created in memory. 
Instead, they only need to iterate over the elements one at a time.

For instance, the following summation code will build a full list of squares in memory, 
iterate over those values, and, when the reference is no longer needed, delete the list:

'''

x = sum([x*x for x in range(10)])

# Memory is conserved by using a generator expression instead:
y = (x*x for x in range(10))
print(y)
# A Generator Object

print(sum(y))

# Now it iterates through it and produces the sum




