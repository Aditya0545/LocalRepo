# Print 10 fibonnaci series 
0,1,1,2,3
t1 = 0
t2 = 1
next = t1+t2
num = int(input("Enter the number that times you wanna get fibonnaci series: "))
print(f"Fibonnaci series are: {t1,t2}")
i = 2
while (i<num):
    print(next)
    t1 = t2
    t2 = next
    next = t1+t2
    i = i+1
    

