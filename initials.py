'''extracting initials from a list of names'''

# Name : Aditya Kumar
# ID : 22BTCSE067

names  = ["Aditya Gupta", "Muskan Ojha", "Noor Ali", "Arshita Navin"]
print(names)
initials = [name.split()[0][0] + "." +name.split()[1][0] for name in names]
print(initials)
# capital_name = [name.capitalize() for name in name_list]
# initial_name = [first[0] for first in capital_name]
# print(initial_name)

# words = ['hello', 'world', 'python']
# uppercase_word = [word.upper() for word in words]
# print(uppercase_word)