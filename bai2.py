A=[ 1,1,2,3,5,8,13,21,34]
B=[ 1,3,5,4,7,88,66,59,40,54]
print("A:",A)
print("B:",B)
C= list( set (A) & set (B))
print( "các phần tử trùng của A vs B là C:", C)
D= list( set (A) ^ set (C))
print("Các phần tử list A ko trùng với B là D:",D)
E= list( set (B) ^ set (C))
print("Các phần tử list B ko trùng với A là E:",E)