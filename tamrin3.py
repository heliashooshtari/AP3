num=int(input("enter a number: "))

for x in range(2,num):
    prime = True
    for i in range(2,x):
        if (x%i==0):
            prime = False
    if prime == True:
       print (x)


print('----------------------------------')
 