a = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
b=[]
lenA=len(a)
for i in range(0,lenA-1):
    if(a[i]<30):
        b.append(a[i])
print(b)