#write a program to print n natural numbers and find its average

sum=0
n=int(input("enter n value:"))
for i in range (1,n+1):
	print(i,end=" ")
	sum=sum+i
	i=i+1
avg=sum/(i-1)
print("\naverage=",avg)