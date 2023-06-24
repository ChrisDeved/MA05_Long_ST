1.
print("Đây là hệ thống quản lí tài liệu File Control System. Vui lòng nhập dữ liệu bạn muốn in.")
t = int(input("Nhập loại tài liệu bạn muốn in (1 là luận văn/báo cáo, 2 là giáo trình(500VND/1 trang)): "))
p = int(input("Nhập số mặt giấy mà bạn muốn in: "))
b = int(input("Nhập số bản sao mà bạn muốn in: "))
if (t == 1):
    print("Số lượng trang giấy cần dùng để in là: ",p * b,"trang" )
    print("Số tiền bạn cần trả để in là: ",(p * b)* 500,"VND")
else:
    print("Số lượng trang giấy cần dùng để in là: ",(p * b) // 2,"trang" )
    print("Số tiền bạn cần trả để in là: ",(p * b) // 2 * 500,"VND")
2.
print("Đây là hệ thống quản lí điện Energize Control System. Vui lòng điền dữ liệu tại đây.")
kilowatt = float(input("Nhập số điện mà hộ gia đình đã sử dụng trong 30 ngày(kWh): "))
if(kilowatt < 50):
    print("Số tiền điện gia đình bạn cần phải trả là: ",kilowatt * 1728,"VND")
elif(51 < kilowatt < 100):
    print("Số tiền điện gia đình bạn cần phải trả là: ",kilowatt * 1768,"VND")
elif(101 < kilowatt < 200):
    print("Số tiền điện gia đình bạn cần phải trả là: ",kilowatt * 2074,"VND")
elif(201 < kilowatt < 300):
    print("Số tiền điện gia đình bạn cần phải trả là: ",kilowatt * 2612,"VND")
elif(300 < kilowatt < 400):
    print("Số tiền điện gia đình bạn cần phải trả là: ",kilowatt * 2919,"VND")
elif(kilowatt > 401):
    print("Số tiền điện gia đình bạn cần phải trả là: ",kilowatt * 3015,"VND")