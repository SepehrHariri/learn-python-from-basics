from functools import reduce

# 1.Square
my_list = [5, 4, 3]

print(list(map(lambda item: item*item, my_list)))

# 2.List Filter
print(list(filter(lambda item: item % 2 != 0, my_list)))

# 3.List Reduce
print(reduce(lambda acc, item: acc+item, my_list))

# 4.List Sorting Based on Second
a = [(0, 2), (4, 3), (9, 9), (10, -2)]

a.sort(key=lambda x: x[1])
print(a)

