score_max = 10
score_cur = 0
print ("Chào mừng bạn đã đến với Examination Questionnare! Bạn sẽ trả lời các câu hỏi để giành điểm số cao.")
print("Trắc nghiệm(3đ): Hãy nhập đáp án đúng:")
print("Câu 1(0,5đ): Giá trị nhỏ nhất của biểu thức |2x - 8| + 2,65 là: ")
ques_mchoose1 = input("A. 2,65; B. 0; C. 2; D. x : ")
print("Câu 2(1đ): Điều kiện để biểu thức 8xy + 6 / 5x + 8 hợp lý là: ")
ques_mchoose2 = input("A. 8xy = 6; B. 5x * 6 = 8xy * 8; C. 5x + 8 > 0; D. 8xy + 6 < 0 : ")
print("Câu 3(0,5đ): Cho MA là tia phân giác của tam giác ABC. Vẽ BF là tia phân giác cắt MA tại G. Cho AB = AC = BC. Hỏi góc BAC = ? ")
ques_mchoose3 = input("A. 45 độ; B. 30 độ; C. 15 độ; D. 90 độ")
print("Câu 2(1đ): Cho BF là đường thẳng cắt ED tại F. Cho ED = 14 cm. Vậy độ dài của EF bằng bao nhiêu cm để BF là đường trung tuyến của tam giác BED? ")
ques_mchoose4 = input("A. 6cm; B. 4cm; C. 7cm; D. Không có độ dài nào hợp lí")
if (ques_mchoose1 == "A",ques_mchoose2 == "C",ques_mchoose3 == "B",ques_mchoose4 == "C"):
    score_cur + 3
elif(ques_mchoose1 != "A",ques_mchoose2 == "C",ques_mchoose3 == "B",ques_mchoose4 == "C"):
    score_cur + 2.5
elif(ques_mchoose1 != "A",ques_mchoose2 != "C",ques_mchoose3 == "B",ques_mchoose4 == "C"):
    score_cur + 1.5
elif(ques_mchoose1 != "A",ques_mchoose2 != "C",ques_mchoose3 != "B",ques_mchoose4 == "C"):
    score_cur + 1
elif(ques_mchoose1 != "A",ques_mchoose2 != "C",ques_mchoose3 != "B",ques_mchoose4 != "C"):
    score_cur + 0
elif(ques_mchoose1 == "A",ques_mchoose2 != "C",ques_mchoose3 == "B",ques_mchoose4 == "C"):
    score_cur + 2
elif(ques_mchoose1 == "A",ques_mchoose2 != "C",ques_mchoose3 != "B",ques_mchoose4 == "C"):
    score_cur + 1.5
elif(ques_mchoose1 == "A",ques_mchoose2 != "C",ques_mchoose3 != "B",ques_mchoose4 != "C"):
    score_cur + 0.5
elif(ques_mchoose1 == "A",ques_mchoose2 == "C",ques_mchoose3 != "B",ques_mchoose4 == "C"):
    score_cur + 2.5
elif(ques_mchoose1 == "A",ques_mchoose2 == "C",ques_mchoose3 != "B",ques_mchoose4 != "C"):
    score_cur + 1.5
elif(ques_mchoose1 == "A",ques_mchoose2 == "C",ques_mchoose3 == "B",ques_mchoose4 != "C"):
    score_cur + 2   
ques2 = float(input("Câu 2(0.5đ): Căn bậc hai số học của 4900 là: "))
if (ques2 == 70):
    print("Chính xác!")
    score_cur + 0.5
else:
    print("Chưa chính xác!")
    score_cur + 0
ques3 = input("Câu 2(1đ): Công thức tính vận tốc là gì?: ")
if (ques3 == "s = v/t"):
    print("Chính xác!")
    score_cur + 1
else:
    print("Chưa chính xác!")
    score_cur + 0
ques4 = input("Câu 3(2đ): Lan đi bộ tới trường trong x(giờ) với vận tốc 10 km/h, sau đó đi xe đạp trong y(giờ) với vận tốc 25 km/h. Viết biếu thức đại số biểu thị quãng đường Lan đi được. Tính giá trị của biểu thức đó khi x = 1; y = 1/4 ")    
if (ques4 == "10x + 25y, 16,25"):
    print("Chính xác!")
    score_cur + 2
else:
    print("Chưa chính xác!")
    score_cur + 0
ques5 = input("Câu 4(1.5đ): Công thức tính diện tích xung quanh, diện tích toàn phần, thể tích hình hộp chữ nhật là gì?(Cho a,b là chiều dài, rộng, h là chiều cao): ")
if (ques5 == "2(a + b) * h, [2(a + b) * h] + 2ab, a * b * h"):
    print("Chính xác!")
    score_cur + 1.5
else:
    print("Chưa chính xác!")
    score_cur + 0
ques6 = input("Câu 5(0.5đ): Tính: 100 - 99 + 98 - 97.... + 4 - 3 + 2 - 1 =" )
if (ques6 == 50):
    print("Chính xác!")
    score_cur + 0.5
else:
    print("Chưa chính xác!")
    score_cur + 0
ques7 = input("Câu 6(1.5đ): Hãy nêu hằng đẳng thức bình phương 1 tổng, 1 hiệu: ")
if (ques7 == "(a + b)^2 = a^2 + 2ab + b^2, (a - b)^2 = a^2 - 2ab + b^2 "):
    print("Chính xác!")
    score_cur + 1.5
else:
    print("Chưa chính xác!")
    score_cur + 0
if (score_cur == score_max):
   print("Chúc mừng bạn đã hoàn thành xuất sắc các câu hỏi với",score_cur,"điểm! Hãy phát huy nhé!")
else:
   print("Chúc mừng bạn đã hoàn thành các câu hỏi với",score_cur,"điểm! Hãy cố gắng hơn vào lần sau nhé!")