list=[1,2,3,4,6,7,]
odd=[]
even=[]
o=0
e=0
sum_even=0
sum_odd=0
for i in range(len(list)):
        if(i % 2 == 0):
            even.append(i)
            o=o+1
            sum_even+=even
        else:
            odd.append(i)
            e=e+1
            sum_odd+=odd
print("even:",even,e)
print("odd:",odd,o)
print(sum_add,sum_odd)
