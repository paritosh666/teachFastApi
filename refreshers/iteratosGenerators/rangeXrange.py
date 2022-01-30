import sys

# x = range(100000000000)

# print (f"The size allotted using range() is : {sys.getsizeof(x)} ")

# o/p: The size allotted using range() is : 48 

# y = (x for x in range(100000000000))

# print (f"The size allotted using range() is : {sys.getsizeof(y)} ")


'''
Using * with generator function to unpack the yielded values

: Called Splat unpacking syntax

'''

# def get_items(val):
#     for i in range(val):
#         yield i

# print(*get_items(10))

# z = (x for x in range(19))
# print(z)


l = [x for x in range(1000000)]
print(f"size of list l is {sys.getsizeof(l)}")

iter_l = iter(l)
print(f"size of iter from list l is {sys.getsizeof(iter_l)}")


tup_iter = tuple(iter_l)
print(f"size of tuple from iter  is {sys.getsizeof(tup_iter)}")



