# list = [43, 9, 6, 72, 8, 11]
# # printing original list
# print("The original number is: ",list)
# for even in list:
#     if not even % 2 :
#         res = even
#         break
# print("The first even element in list is : " + str(res))


num = int(input("enter the number: "))
while num%2 !=0:
    num += 1
print("first even number: ",num)