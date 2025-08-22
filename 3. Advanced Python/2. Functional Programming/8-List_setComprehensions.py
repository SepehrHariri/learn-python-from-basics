# Lists Comprehensions
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)


# Sets Comprehensions
my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0,100)}
my_set3 = {num**2 for num in range(0,100)}
my_set4 = {num**2 for num in range(0,100) if num % 2 == 0}

print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)