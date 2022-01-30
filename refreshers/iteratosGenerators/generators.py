# https://docs.python.org/3/howto/functional.html#generators

'''
Generators are a special class of functions that simplify the task of writing iterators.
Regular functions compute a value and return it, 
but generators return an iterator that returns a stream of values.
'''


# COMMON USE CASE OF GENERATOR FUNCTIONS

'''
When you call a function, it gets a private namespace where its local variables are created. 
When the function reaches a return statement, 
the local variables are destroyed and the value is returned to the caller. 
A later call to the same function creates a new private namespace and a fresh set of local variables. 
But, what if the local variables weren't thrown away on exiting a function? 
What if you could later resume the function where it left off? 
This is what generators provide; they can be thought of as resumable functions.
'''

# Here’s the simplest example of a generator function:

def generate_ints(N):
   for i in range(N):
       yield i


print(generate_ints(10))
# O/P: <generator object generate_ints at 0x10451c0b0>

print(generate_ints(10).__next__()) 
# O/P: 0
print(generate_ints(10).__next__()) 
# O/P: 1
print(generate_ints(10).__next__()) 
# O/P: 2
print(generate_ints(10).__next__()) 
# O/P: 3


'''
Any function containing a yield keyword is a generator function; 
this is detected by Python's bytecode compiler which compiles the function specially as a result.

When you call a generator function, it doesn't return a single value; instead it returns a generator object that supports the iterator protocol. 
On executing the yield expression, the generator outputs the value of i, similar to a return statement. 
The big difference between yield and a return statement is that on reaching a yield the generator's
 state of execution is suspended and local variables are preserved. 
 On the next call to the generator’s __next__() method, the function will resume executing.

'''

# Generators also support Upacking

a,b,c = generate_ints(3)
print(a,b,c)


# Or you can run good old for loop

for i in generate_ints(3):
    print(i)
