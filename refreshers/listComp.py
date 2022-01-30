x = [i for i in range(10)]
print(x)

# Equivalent to:

for i in range(10):
    print(i)


# ----------------------------------------- #

y = [x*x if x%2==0 else 0 for x in range(10) ]
print(y)

# equivalent to

for x in range(10):
    if x % 2 == 0:
        print(x*x)
    else:
        print(0)


# NESTED IF ELSE IN LIST COMP 
print("-------------------------------------")

# for i in range(10):
#     for j in range(10,20):
#         if i+j % 2 == 0:
#             print("yeah")
#         else:
#             print("oh! No!!!")

z = iter(["Additive Even" if i+j%2==0 else "Additive Odd" for i in range(10) for j in range(10,20)] )
print(next(z))
print(next(z))
print(next(z))
print(next(z))


