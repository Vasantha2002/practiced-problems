n=int(input("enter n value:\n"))
temp=0
while n!=0:
	temp=n%10
	print(temp,end="")
	n=n//10
