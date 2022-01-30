#  Text From the docs
# https://docs.python.org/3/howto/functional.html

'''
What is an Iterator?

An iterator is an object representing a stream of data; 
this object returns the data one element at a time. 

A Python iterator must support a method called __next__() that takes no arguments and always 
returns the next element of the stream. 
If there are no more elements in the stream, __next__() must raise the StopIteration exception.
Iterators don't have to be finite, though; 
it's perfectly reasonable to write an iterator that produces an infinite stream of data.

'''


lst = [1,2,3,4,5]
iter_lst = iter(lst)

'''
The built-in iter() function takes an arbitrary object 
and tries to return an iterator that will return the object's contents or elements, 
raising TypeError if the object doesn't support iteration.
'''

print(iter_lst)

print(iter_lst.__next__())
# OR
print(next(iter_lst))
print(next(iter_lst))
print(next(iter_lst))
print(next(iter_lst))


# print(next(iter_lst))  
# Raises StopIteration Exception ; end of the list


print("0----------------0")

'''
Python expects iterable objects in several different contexts, 
the most important being the for statement. In the statement for X in Y, 
Y must be an iterator or some object for which iter() can create an iterator.
These two statements are equivalent:


for i in iter(lst):
    print(i)

for i in lst:
    print(i)

'''


# Iterators can be materialized as lists or tuples by using the list() or tuple() constructor functions:

back_to_list = list(iter([x for x in range(10)]))
# print(back_to_list)

# Iters also support built in max(), min(), sum() methods.
init_iter = iter([x for x in range(10)])
# print(sum(init_iter))

# print(min(iter([x for x in range(10)])))

a = {'Italy': 'Rome', 'France': 'Paris', 'US': 'Washington DC'}
print(iter(a).__next__())
# Only creates an iter of the keys


print(iter(a.values()).__next__())
# Returns the  values and an iter


print(iter(a.items()).__next__())
# Returns a tuple with the key an value
# o/p:  ('Italy', 'Rome')
