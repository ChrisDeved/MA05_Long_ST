print("BT1:")
print("Chào mừng các bạn đến với Money Calculator. Vui lòng nhập số tiền bạn muốn quy đổi.")
money = float(input("Số tiền mà bạn muốn quy đổi(USD -> VND): $ "))
print("Số tiền quy đổi từ USD -> VND: VND",money * 23480)
money1 = float(input("Số tiền mà bạn muốn quy đổi(VND -> USD): VND "))
print("Số tiền quy đổi từ VND -> USD: $",money1 / 23480)
money2 = float(input("Số tiền mà bạn muốn quy đổi(GBP -> VND): £ "))
print("Số tiền quy đổi từ GBP -> VND: VND",money2 * 29515)
money3 = float(input("Số tiền mà bạn muốn quy đổi(VND -> GBP): VND"))
print("Số tiền quy đổi từ VND -> GBP: £",money3 / 29515)
money4 = float(input("Số tiền mà bạn muốn quy đổi(EUR -> VND): 	€ "))
print("Số tiền quy đổi từ EUR -> VND: VND",money4 * 25249)
money5 = float(input("Số tiền mà bạn muốn quy đổi(VND -> EUR): VND"))
print("Số tiền quy đổi từ VND -> EUR: €",money5 / 25249)
money6 = float(input("Số tiền mà bạn muốn quy đổi(KWD -> VND):	د.ك"))
print("Số tiền quy đổi từ KWD -> VND: VND",money6 * 76894)
money7 = float(input("Số tiền mà bạn muốn quy đổi(VND - > KWD): VND "))
print("Số tiền quy đổi từ KWD -> VND:د.ك  ",money7 / 76894)
print("BT2:")
print("Đây là hệ thống tính chu vi - diện tích Circle Calculator. Vui lòng nhập giá trị bán kính.")
radius1 = int(input("Bạn hãy nhập bán kính của hình tròn(cm): "))
print("Chu vi của hình tròn tính theo cm là: ",2 * radius1 * 3,14)
print("Diện tích của hình tròn tính theo cm là: ",radius1^2 * 3,14)
print("BT3:")
print("Đây là hệ thống tính thời gian trung bình Timing Calculator. Vui lòng nhập giá trị để tính.")
time1 = float(input("Thời gian của VĐV thứ nhất(s): "))
time2 = float(input("Thời gian của VĐV thứ hai(s): "))
time3 = float(input("Thời gian của VĐV thứ ba(s): "))
print("Thời gian trung bình của cả 3 VĐV (s) là: ",(time1 + time2 + time3)/3)