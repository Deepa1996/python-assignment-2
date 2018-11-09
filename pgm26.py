str=input("Enter the string to be converted uppercase: ")

for i in range(len(str)):

   x=ord(str[i])
   if x>=97 and x<=122:
       x=x-32
   y=chr(x)
   print(y,end="")
   	