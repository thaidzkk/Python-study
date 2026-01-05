#1. In ra kiểu dữ liệu của biến
x = 10
print(type(x))      # Output: <class 'int'>
y = True                    
print(type(y))      # Output: <class 'bool'>    


#2. Hàm input() để nhập dữ liệu từ người dùng                
name = input("Nhập gì đó: ")        # Input từ người dùng luôn là chuỗi (string)
print(name)     # Output: giá trị người dùng nhập vào


#3. Chuyển kiểu dữ liệu
name2 = int(name)   # Chuyển chuỗi sang số nguyên (int) 
print(type(name2))   # Output: <class 'int'>


#4. Phép toán với chuỗi và số
x2 = "3" * 3   # Phép nhân chuỗi
print(x2)   # Output: 333
x3 = int("3") * 3   # Chuyển chuỗi "3" sang số nguyên rồi nhân với 3
print(x3)   # Output: 9


#5. Nhúng giá trị biến vào chuỗi
x = 20
print("i am " + str(x))     # Output: i am 20
# Using f-string
print(f"i am {x}")      # Output: i am 20


#6. Các phương thức thường dùng với chuỗi
s = "hello world"
s = s.capitalize()   # Viết hoa chữ cái đầu tiên, output: Hello world
s = s.title()        # Viết hoa chữ cái đầu tiên của mỗi từ, output: Hello World
s = s.upper()        # Viết hoa tất cả các chữ cái, output: HELLO WORLD
s = s.lower()        # Viết thường tất cả các chữ cái, output: hello world
s = s.strip()        # Xóa khoảng trắng thừa ở đầu và cuối chuỗi, output: "hello world"
s = s.replace("world", "Python")   # Thay thế từ "world" bằng "Python", output: hello Python
s = s.split(" ")    # Tách chuỗi thành danh sách các từ, output: ['hello', 'Python']


#7. Kiểu dữ liệu Boolean
# True và False (chữ cái đầu viết hoa)
bool(1)   # True
bool(0)   # False
bool(-1)  # True
bool(0j)  # False


#8. Toán tử
# Toán tử số học: +, -, *, /, %, //, **
""""
- Dùng // cho phép chia lấy phần nguyên
- Dùng ** cho phép lũy thừa 
- Khi nối chuỗi, tránh + trong vòng lặp vì nó tạo ra nhiều bản sao tạm thời, làm chậm hiệu suất. 
  Thay vào đó, sử dụng phương pháp join() để nối chuỗi hiệu quả hơn.
- Dùng % để lấy phần dư của phép chia
"""

# Toán tử so sánh: ==, !=, >, <, >=, <=

# Toán tử logic: and, or, not
print(1 and 5)   # Output: 5, vì 1 là True, nên trả về giá trị cuối cùng
print(0 and 5)    # Output: 0, vì 0 là False, nên trả về giá trị đầu tiên
print(1 or 5)    # Output: 1, vì 1 là True, nên trả về giá trị đầu tiên
print(0 or 5)     # Output: 5, vì 0 là False, nên trả về giá trị cuối cùng

# Toán tử gán: =, +=, -=, *=, /=, %=, //=, **=

# Toán tử đặc biệt: is, is not, in, not in
 
# Toán tử bitwise: &, |, ^, ~, <<, >>


#9. List và các phương thức thường dùng với List
my_list = [1, 2, 3, 4, 5]
my_list[1]      # Truy cập phần tử tại vị trí index 1, output: 2
my_list[-1]     # Truy cập phần tử cuối cùng trong danh sách, output: 5
my_list[0] = 9            # Thay đổi giá trị phần tử tại vị trí index 0 thành 9, output: [9, 2, 3, 4, 5]
my_list.index(1)       # Tìm vị trí index của giá trị 1 trong danh sách, output: 0
my_list.append(6)        # Thêm phần tử vào cuối danh sách, output: [9, 2, 3, 4, 5, 6]
my_list.insert(1, 0)     # Chèn phần tử 0 vào vị trí index 1, output: [9, 0, 2, 3, 4, 5, 6]
my_list.remove(3)        # Xóa phần tử có giá trị 3 khỏi danh sách, output: [9, 0, 2, 4, 5, 6]
del my_list[-2]        # Xóa phần tử tại vị trí index -2, output: [9, 0, 2, 4, 6]
my_list.pop()          # Xóa và trả về phần tử cuối cùng trong danh sách, output: 6, danh sách còn lại: [9, 0, 2, 4]
my_list.sort()           # Sắp xếp danh sách theo thứ tự tăng dần, output: [0, 2, 4, 9]
my_list.sort(reverse=True)  # Sắp xếp danh sách theo thứ tự giảm dần, output: [9, 4, 2, 0]
my_list.reverse()        # Đảo ngược thứ tự danh sách, output: [0, 2, 4, 9]
my_list.extend([7, 8, 9])  # Mở rộng danh sách bằng cách thêm các phần tử từ một danh sách khác, output: [0, 2, 4, 9, 7, 8, 9]
my_list.count(9)        # Đếm số lần xuất hiện của giá trị 9 trong danh sách, output: 2
len(my_list)           # Lấy độ dài của danh sách, output: 8
my_list.clear()          # Xóa tất cả các phần tử trong danh sách, output: []

my_list2 = [1, 2, 3, 4, 5]
max(my_list2)        # Tìm giá trị lớn nhất trong danh sách, output: 5
min(my_list2)         # Tìm giá trị nhỏ nhất trong danh sách, output: 1
sum(my_list2)        # Tính tổng các phần tử trong danh sách, output: 15

# List lồng nhau, truy cập phần tử trong list lồng nhau
my_list3 = [[Romeo, 15], [Juliet, 14], [Mercutio, 16]]
print(my_list3[0][0])   # Output: Romeo
print(my_list3[1][1])   # Output: 14

# Sao chép danh sách và so sánh danh sách
lst1 = [1, 2, 3]
lst2 = lst1.copy()   # Tạo bản sao của lst1
lst3 = lst2
print(lst2 is lst1)   # Output: False, vì lst2 và lst1 là hai đối tượng khác nhau trong bộ nhớ
print(lst3 is lst1)   # Output: True, vì lst3 tham chiếu đến cùng một đối tượng với lst1
print(lst2 == lst1)   # Output: True, vì lst2 và lst1 có cùng giá trị
print(lst3 == lst1)   # Output: True, vì lst3 và lst1 có cùng giá trị

# Cắt List (list slicing), a = listname[start:stop:step]
lst4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
newlst4 = lst4[1:4]   # Tạo một danh sách mới từ lst4, bao gồm các phần tử từ index 1 đến index 3, output: [20, 30, 40]
newlst5 = lst4[1:9:2]  # Tạo một danh sách mới từ lst4, bao gồm các phần tử từ index 1 đến index 8, với bước nhảy là 2, output: [20, 40, 60, 80]
newlst6 = lst4[::2]    # Tạo một danh sách mới từ lst4, bao gồm tất cả các phần tử với bước nhảy là 2, output: [10, 30, 50, 70, 90]
newlst7 = lst4[::-2]  # Tạo một danh sách mới từ lst4, bao gồm tất cả các phần tử với bước nhảy là -2 (đảo ngược), output: [100, 80, 60, 40, 20]
newlst8 = lst4[:]      # Tạo một bản sao của lst4, output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
newlst9 = lst4[:9]     # Tạo một danh sách mới từ lst4, bao gồm các phần tử từ đầu đến index 8, output: [10, 20, 30, 40, 50, 60, 70, 80, 90]
newlst10 = lst4[5:]     # Tạo một danh sách mới từ lst4, bao gồm các phần tử từ index 5 đến cuối danh sách, output: [60, 70, 80, 90, 100]
newlst11 = lst4[5::2]  # Tạo một danh sách mới từ lst4, bao gồm các phần tử từ index 5 đến cuối danh sách, với bước nhảy là 2, output: [60, 80, 100]



#10. Tuple và các phương thức thường dùng với Tuple
"""
- Tuple khác với list ở chỗ list là kiểu dữ liệu có thể thay đổi (mutable).
- Tuple là kiểu dữ liệu không thể thay đổi (immutable), tức là sau khi tạo, không thể thêm, xóa hoặc thay đổi các phần tử trong tuple.
- Tuple được tạo bằng cách sử dụng dấu ngoặc đơn ().
- Các phần tử trong tuple có thể là các kiểu dữ liệu khác nhau, bao gồm cả list và tuple khác.
- Tuple hỗ trợ các phương thức như count() và index().
- Tuple thường được sử dụng khi muốn lưu trữ một tập hợp các giá trị mà không cần thay đổi chúng.
- Tuple có hiệu suất nhanh hơn list trong một số trường hợp do tính bất biến của nó.
"""
my_tuple1 = (1, 2, 3, 4, 5)
my_tuple1[0]      # Truy cập phần tử tại vị trí index 0, output: 1
my_tuple1[-1]    # Truy cập phần tử cuối cùng trong tuple, output: 5
my_tuple1[1] = 9    # Lỗi, vì tuple không thể thay đổi giá trị phần tử
my_tuple1.append(6)   # Lỗi, vì tuple không thể thêm phần tử mới
my_tuple1 += (6, 7)   # Tạo một tuple mới bằng cách nối my_tuple1 với một tuple khác, output: (1, 2, 3, 4, 5, 6, 7)
my_tuple1.index(3)   # Tìm vị trí index của giá trị 3 trong tuple, output: 2
my_tuple1.count(2)   # Đếm số lần xuất hiện của giá trị 2 trong tuple, output: 1
len(my_tuple1)     # Lấy độ dài của tuple, output: 5
my_tuple2 = (10, 20, 30, 40, 50)
max(my_tuple2)      # Tìm giá trị lớn nhất trong tuple, output: 50
min(my_tuple2)       # Tìm giá trị nhỏ nhất trong tuple, output: 10
sum(my_tuple2)      # Tính tổng các phần tử trong tuple, output: 150
# Tuple lồng nhau, truy cập phần tử trong tuple lồng nhau
my_tuple3 = (("Alice", 30), ("Bob", 25), ("Charlie", 35))
print(my_tuple3[0][0])   # Output: Alice
print(my_tuple3[1][1])   # Output: 25     



#11. Set và các phương thức thường dùng với Set
"""
- Set là một kiểu dữ liệu trong Python dùng để lưu trữ một tập hợp các phần tử không trùng lặp và không có thứ tự cụ thể.
- Set được tạo bằng cách sử dụng dấu ngoặc nhọn {} hoặc hàm set().
- Các phần tử trong set phải là các kiểu dữ liệu không thể thay đổi (immutable), như số, chuỗi, hoặc tuple.
- Set hỗ trợ các phép toán tập hợp như hợp (union), giao (intersection), hiệu (difference) và hiệu đối xứng (symmetric difference).
- Set không hỗ trợ truy cập phần tử theo chỉ số vì nó không có thứ tự.
- Set thường được sử dụng khi cần lưu trữ các phần tử duy nhất và thực hiện các phép toán tập hợp.
"""
my_set = {1, 2, 3, 4, 5}
my_set.add(6)          # Thêm phần tử vào set, output: {1, 2, 3, 4, 5, 6}
my_set.remove(3)     # Xóa phần tử khỏi set, output: {1, 2, 4, 5, 6}
my_set.discard(10)   # Xóa phần tử khỏi set nếu tồn tại, không gây lỗi nếu phần tử không tồn tại
my_set.pop()         # Xóa và trả về một phần tử ngẫu nhiên từ set, output: một số trong set
my_set.clear()       # Xóa tất cả các phần tử trong set, output: set()  



