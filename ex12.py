#To print sum for the given series 1+1/2+2/3+.......+n/n+1

n=int(input("enter n value: "))
sum=0
for i in range(1,n+1):
	sum=sum+(i/i+1)
print(sum)
