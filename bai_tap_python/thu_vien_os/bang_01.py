import os
# In ra màn hình thư mục làm việc hiện tại của chương trình

tm = os.getcwd()
print("thư mục làm việc hiện tại:", tm)

# Chuyển đến thư mục: ‘D:/data’,
#sau đó in thư mục hiện tại ra màn hình

os.chdir('F:\\data')
tmf = os.getcwd()

print("thư mục hiện tại:", tmf)

# Tạo thư mục con có tên là ‘nnlt’,
# sử dụng hàm makedirs()

directory = "nnlt"
d_d = "F:\\data"
path = os.path.join(d_d, directory)
os.makedirs(path)
print("thư mục con của",d_d,"là:", directory)

#Liệt kê tất cả các tập tin và thư mục có trong thư mục ‘My Documents’
# trên máy tính của bạn và in ra màn hình

d_d1 = "C:/Users/Duc/Documents"
dir_list = os.listdir(d_d1)

print(" các tập tin và thư mục có trong'", d_d1, "' :\n",dir_list)

#Kiểm tra 1 file (tự nhập đường dẫn và tên tập tin gồm cả phần mở rộng)
# có tồn tại trong máy hay không, sử dụng hàm os.path.exists()

path = 'nnnlt'
isExist = os.path.exists(path)
print(isExist)

# Xóa 1 thư mục và xóa 1 file trong máy tính

vt = "F:/data/"
file = 'nn.txt'
file1 = 'nnnnlt'

path = os.path.join(vt, file)
path1 = os.path.join(vt, file1)
os.remove(path)
os.rmdir(path1)
