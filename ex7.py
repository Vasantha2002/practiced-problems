#write a program to convert binary to decimal

bn=int(input("enter a value:"))
dn=0
i=0
while bn!=0:
	r=bn%10
	dn=dn+r*(2**i)
	bn=bn//10
      i=i+1
print("the decimal value is : ",dn)
