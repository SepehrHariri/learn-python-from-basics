# Write a program to find the sum of items in the list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12]

# 1.solution

total_1 = 0
for item in my_list:
    total_1 += item

print(total_1)

print("\t")
# 2.solution

total_2 = sum(my_list)

print(total_2)