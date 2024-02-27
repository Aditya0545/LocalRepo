'''Create a program that performs the following operation on alist of integers : 
    * appends an element to the end of the list
    * insert an element at an specific position in the list
    * remove an element fom the list by value 
    * print the final list'''

# Name: Aditya kumar
# ID : 22BTCSE067

list = [2,4,6,8,9,12]
print(list)
appended = int(input("Enter the element to append: "))
list.append(appended)
print(f"Appended list is {list}")

inserted = int(input("Enter the element to insert: "))
index_no = int(input("Enter the index number: "))
list.insert(index_no,inserted)
print(f"Inserted list is {list}")

removed = int(input("select the element to remove from the list: "))
list.remove(removed)
print(f"list after removing selected element is {list}")

print(f"Final list is {list}")