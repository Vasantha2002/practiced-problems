#program to print sum for fraction of series

n=int(input("enter n value:"))
sum=0
for i in range(1,n+1):
	sum=sum+(1/i)
print("sum of fraction series",sum)
	