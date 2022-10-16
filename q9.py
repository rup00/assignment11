n=int(input("enter the number to find the eqvivalent binary number"))
a=[]
while n>0:
    x=n%2
    a.append(x)
    n=n//2
    a.reverse()
print("binary number:")
for i in a:
    print(i,end=" ")
