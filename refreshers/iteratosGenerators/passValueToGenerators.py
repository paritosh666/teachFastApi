# def counter(maximum):
#     i = 0
#     while i < maximum:
#         val = (yield i)
#         # If value provided, change counter
#         if val is not None:
#             i = val
#         else:
#             i += 1


# print(counter(10).__next__())
# print(counter(10).send(8))


print((x for x in [1,2,3,4,5,6,7]))