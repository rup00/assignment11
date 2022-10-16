n=int(input("enter the n number to sum of first n even numbers"))
m=n*2
sum=0
for i in range(1,m+1):
    if(i%2==0):
        sum+=i
print(sum)
