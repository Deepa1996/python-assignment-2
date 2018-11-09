import sys
f=open("example.txt","a+")
a=sys.argv[1]
b=sys.argv[2]
f.write(a)
f.write(b)
print(a,b)
