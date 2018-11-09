def circle(x):
	return 3.14*x*x
def triangle(x,y):
	return 0.5 *x*y
def square(x):
	return x*x
print("enter the choice:")
print("1.circle")
print("2.triangle")
print("3.rectangle")
choice=input("enter the choice:(1/2/3)")
num1=int(input("enter the value"))
num2=int(input("enter the value"))
if choice == '1':
	 print(3.14,"*",num1,"*",num1,"=",circle(num1))
elif choice =='2':
	print(0.5,"*",x,"*",y,"=",triangle(num1,num2))
elif choice =='3':
	print(x,"*",x,"=",square(num1))
else:
	print("invaid")

