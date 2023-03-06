#program to print sum of the digits in a given number

n=int(input("enter a number:\n"))
sum=r=0
while n!=0:
	r=n%10
	sum=sum+r
	n=n//10
print("sum=",sum)


	
	
