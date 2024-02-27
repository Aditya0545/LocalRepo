# Repeat the String 
def string_repeat(string,times):
    repeated = (string+"\n") * times
    return repeated

entered_string = str(input("Enter Your String: "))
repeat = int(input("Enter the times to repeat string: "))

result = string_repeat(entered_string, repeat)
print(result)