#program to print sum for n odd and n even numbers

n=int(input("enter number:"))
sum1=sum2=i=0
while i<=n:
	if i%2==0:
		sum1=sum1+i
		i=i+1
	else:
		sum2=sum2+i
		i=i+1
print("\nsum of odd numbers",sum1)
print("\nsum of even numbers",sum2)
