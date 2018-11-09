#28. Implement a progam to convert the input string to inverse case(upper->lower, lower->upper) ( without using standard library)
str=input("enter the string in uppercase letter\n")
g=''
for char in str:
	if ord(char)>=97 and ord(char)<=122:
		result=ord(char) - 32
		y=chr(result)
		g=g+y
for char in str:
	if ord(char)>=65 and ord(char)<=96:
		result=ord(char) + 32
		y=chr(result)
		g=g+y

print(g)