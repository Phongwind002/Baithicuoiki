def  ten(n):
    ten = 0
    while ( n >0):
        ten = ten + n % 10
        n = int (n / 10)
    return ten
a = input("Nhập tên đệm n =") 
n=len(a)
print("Tổng các chữ số của" , n , "là" , ten(n))