#nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))
# kiểm tra xem số đÓ có phải số chẵn hay không
if so % 2 == 0:
    print(so, "là số chẳn.")
else:
    print(so, "không phải số chẳn.")
