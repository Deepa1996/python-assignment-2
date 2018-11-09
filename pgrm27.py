str=input("Enter the string to be converted lowercase: ")

for i in range(len(str)):

   x=ord(str[i])
   if x>=65 and x<=96:
       x=x+32
   y=chr(x)
   print(y,end="")
   	