#program to print factorial of a given number

n=int(input("enter n value: "))
fact=1
for i in range(1,n+1,1):
	fact=fact*i
print(fact)