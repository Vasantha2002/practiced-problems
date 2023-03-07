#write a program to calculate the the sum of even digits and odd digits and their absol.difference

n=int(input("enter a number:"))
temp=0
sum1=sum2=0
while n!=0:
	temp=n%10
	if(temp%2==0):
		sum1=sum1+temp
	else:
		sum2=sum2+temp
	n=n//10

print("difference of even and odd ", abs(sum1-sum2))
