def multiply(x, y):
    return x * y


items = [1, 2, 3]
items2 = [4, 5, 6]
out = [i for i in map(multiply, items, items2)]
out_multi_by_3 = [i for i in map(lambda x: x * 3, items)]
print(out)
print(out_multi_by_3)
