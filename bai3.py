n= int(input(" nhập số cần tính giai thừa : "))
def giaithua(n):
    if(n<0):
       n= int(input("lỗi! Nhập lại n: "))
    if n==0:
        return 1
    return  n* giaithua(n-1)
print("Giai thừa của sô can tim là:",giaithua(n))