n = input("Nhập tên n =")
a=str(n)
dodaiten = len(a)
d=dict()
for i in range(1, dodaiten +1):
    d[i] = i * i
print (d)