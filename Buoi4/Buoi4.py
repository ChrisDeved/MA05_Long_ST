
a = True
b = False
c = True

n = int(input("Vui lòng nhập số n:"))
if (n % 2 == 0):
    print (n, "là số chẵn.")
else:
    print (n, "là số lẻ.")

print("Chọn 1. Là quả tảo")
print("Chọn 2. Là quả cam")
print("Chọn 3. Là quả xoài")
print("Chọn 4. Là các quả còn lại")

quả = int(input("Nhập quả cần bỏ vào giỏ: "))
if (quả == 1):
    print("Bỏ vào giỏ A")
elif (quả == 2):
    print("Bỏ vào giỏ B")
elif (quả == 3):
    print("Bỏ vào giỏ C")
else:
    print("Bỏ vào giỏ D")

số = float(input("Nhập số: "))
if (số >= 0):
    print("Giá trị tuyệt đối của",số, "là:",round(số))
elif (số <= 0):
    print("Giá trị tuyệt đối của",số,"là:",round(số * (-1)))