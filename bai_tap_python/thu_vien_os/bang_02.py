import os
os.chdir('F:\\data')
tmf = os.getcwd()

print("thư mục hiện tại:", tmf)

# Mở 1 tập tin văn bản (đường dẫn và tên file do bạn tự xác định) để đọc
f = open("BÀI 12.xlsx","r")

# Mở 1 tập tin văn bản (đường dẫn và tên file do bạn tự xác định) để ghi
f1 = open("BÀI 12.xlsx","ta")

# Mở tập tin nhị phân (đường dẫn và tên file do bạn tự xác định;
# có thể chọn 1 file ảnh) để đọc và ghi
f2 = open("anh.jpg","rb+")

# Mở 1 tập tin văn bản để đọc, biết các kí tự của tập tin này tuân theo chuẩn Unicode – UTF-8
f3 = open("Ma-trận.docx","rt+",encoding= "utf-8")

# Thao tác đóng tập tin
f.close()

#Mở tập tin văn bản để đọc bằng cấu trúc câu lệnh
# try:....finally:....
try:
   f = open("Ma-trận.docx", encoding = 'utf-8')
finally:
   f.close()

# Mở tập tin văn bản để đọc bằng cấu trúc: with ... as f:
with open("Ma-trận.docx", encoding = 'utf-8') as f3:
    f3.close()

# Mở tập tin văn bản Unicode và ghi vào 3 dòng có nội dung tùy ý bạn
f4 = open("ma tran.txt","t+a", encoding = 'utf-8')
f4.write("urtuyutyuu")

#Mở tập tin văn bản Unicode,
# đọc toàn bộ nội dung của văn bản và in ra màn hình
doc=f4.read()
print(doc)
f4.close()

#Mở tập tin nhị phân (chọn 1 bức ảnh),
# đọc và ghi toàn bộ nội dung tập tin ra màn hình.
f2 = open("anh.jpg","rb+")
doc=f2.read()
print(doc)
f2.close()