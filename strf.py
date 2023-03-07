#program to implement string functions


x='vasantha'
y='659'
z='va va va va'
a=   '   vasantha lakshmi   '
b='Donkey And Monkey'
c='abc,def,ghi,jkl'
txt='my name is vasantha'
d='vasantha2002'

print(max(x))

print(min(x))

print(max(y))

print(min(y))

print(z.replace('v','l')) 		#replaces letters

print(a.lstrip())				#removes spaces

print(b.swapcase()) 			#changes upper to lower and vice versa
 
print(c.split(','))   			#splits each of the word by using given delimator
print('-'.join(['abc','def']))

print(list(enumerate(txt)))  		#represent index of each letter gives in a set of list

print(d.isnumeric())  			#gives numericals

print(d.isalpha())   			#gives alphabets

print(z.isupper())     			#checks upper cases return boolean true r false

print(z.islower())     			#checks lower

print(z.isspace())     			#checks spaces