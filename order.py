# Define a list
my_list = [1, 2, 3, 4, 5]

# Using a while loop to iterate through the list in forward order
print("Forward order using while loop:")
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# Using a while loop to iterate through the list in reverse order
print("\nReverse order using while loop:")
i = len(my_list) - 1
while i >= 0:
    print(my_list[i])
    i -= 1

# Using a for loop to iterate through the list in forward order
print("\nForward order using for loop:")
for item in my_list:
    print(item)

# Using a for loop to iterate through the list in reverse order
print("\nReverse order using for loop:")
for item in reversed(my_list):
    print(item)