def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def mul(x,y):
	return x*y
def divide():
	return x/y
print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.divide")

choice=input("enter your operation(1/2/3/4):")
num1=int(input("enter the first num:"))
num2=int(input("enter the second num:"))

if choice == '1':
	print(num1,"+",num2,"=",add(num1,num2))
elif choice =='2':
	print(num1,"-",num2,"=",sub(num1,num2))
elif choice =='3':
	print(num1,"*",num2,"=",mul(num1,num2))
elif choice =='4':
	print(num1,"/",num2,"=",divide(num1,num2))
else:
	print("invalid input")



