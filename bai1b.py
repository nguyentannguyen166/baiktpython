B=[1,1,1,6,8,9,5,6,45,3,4,66,44,37,78]
C=[]
lenB=len(B)
n=int(input("nhap so can xet:"))
for x in range(0,lenB-1):
    for y in range(x,lenB):
        if(B[x]>B[y]):
            temp=B[y]
            B[y]=B[x]
            B[x]=temp
for z in range (0,lenB):
    if(B[z]>n):
        C.append(B[z])
        print(C)
