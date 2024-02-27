'''Write a program that performs the following operation ona list of string
    * extract a sublist from index 1 to 3
    * extract every alternate element from the list
    * reverse the list'''

    # Name: Aditya Kumar
    # ID : 22BTCSE067

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"sublist from index 1 to 3 is {list[1:4]}")

print(f"Every alternate element is {list[0:7:2]}")

list.reverse()
print(f"Reversed list is {list}")