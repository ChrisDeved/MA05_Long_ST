'''
x = "$23.000.000"
y = "Renato"
z = "Sanches"
t = 9
print("Price = ",x)
print("Name = ",y,z)
print("Result: SIGNING SUCCESS =>",x,y,z)
print("Lilie LOSC -> Paris Saint Germain")
print("Shirt Number:",t)


#comment
# Họ và tên: Nguyễn Ngọc Long

#print("Bạn là ai: ", input("Họ và tên:"))

Tên = input("Tên của bạn: ")
Họ_đệm = input("Họ và tên đệm của bạn: ")
Tuổi = input("Tuổi của bạn là bao nhiêu: ")

print("Tên đầy đủ của bạn là: ", Họ_đệm, Tên)
print("Tuổi hiện tại là: ", Tuổi)

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c = "))
print("Kết quả = ",(a + b + c) / 3)
'''
print("Chào mừng các bạn đến với Money Calculator. Vui lòng nhập số tiền bạn muốn quy đổi.")
money = float(input("Số tiền mà bạn muốn quy đổi(USD -> VND): $ "))
print("Số tiền quy đổi từ USD -> VND: VND",money * 23000)
money1 = float(input("Số tiền mà bạn muốn quy đổi(VND -> USD): VND "))
print("Số tiền quy đổi từ VND -> USD: $", money1 / 23000)
moneytime = float(input("Hãy nhập số tiền bạn làm được trong 1 tháng: $ "))
moneyneed = float(input("Nhập số tiền bạn cần: $"))
print("Vậy để đạt được số tiền đó bạn cần thời gian (tháng) là: $",moneyneed / moneytime)
print("Quy đổi ra VND là: VND",(moneytime / moneyneed) * 23000)