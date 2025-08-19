my_list = [1,2,3]
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list) # Pure function Not change my_list