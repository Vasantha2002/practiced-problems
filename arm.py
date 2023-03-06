n=int(input("enter a number: "))
temp=n
s=0
while n!=0:
	r=n%10
	s=s+(r*r*r)
	n=n//10
if(temp==s):
	print(s,"is an armstrong number")
else:
	print(s,"is not an armstrong number")