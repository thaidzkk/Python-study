#1. In ra kiểu dữ liệu của biến
x = 10
print(type(x))      # Output: <class 'int'>
y = True                    
print(type(y))      # Output: <class 'bool'>    


#2. Hàm input() để nhập dữ liệu từ người dùng                
name = input("Nhập gì đó: ")        # Input từ người dùng luôn là chuỗi (string)
print(name)     # Output: giá trị người dùng nhập vào


#3. Ép kiểu dữ liệu
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
s = s.split(" ")    # Tách chuỗi thành list các từ, output: ['hello', 'Python']


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


=====================================================================================
=====================================================================================

# BÀI 9: List và các phương thức thường dùng với List
"""
- List là một kiểu dữ liệu trong Python dùng để lưu trữ một tập hợp các phần tử có thể thay đổi (mutable) và có thứ tự.
- List được tạo bằng cách sử dụng dấu ngoặc vuông [].
- Các phần tử trong list có thể là các kiểu dữ liệu khác nhau, bao gồm cả list và tuple khác.
- List hỗ trợ các phương thức như append(), insert(), remove(), pop(), sort(), reverse(), extend(), count(), index(), clear() và nhiều phương thức khác.
- List có thể được truy cập bằng chỉ số (index), bắt đầu từ 0 cho phần tử đầu tiên, và có thể sử dụng chỉ số âm để truy cập từ cuối list.
- List có thể được cắt (slicing) để tạo ra một list con từ list gốc.
- List thường được sử dụng khi cần lưu trữ và thao tác với một tập hợp các phần tử có thể thay đổi.
"""

# Ví dụ 1
my_list = [1, 2, 3, 4, 5]
my_list[1]      # Truy cập phần tử tại vị trí index 1, output: 2
my_list[-1]     # Truy cập phần tử cuối cùng trong list, output: 5
my_list[0] = 9            # Thay đổi giá trị phần tử tại vị trí index 0 thành 9, output: [9, 2, 3, 4, 5]
my_list.index(1)       # Tìm vị trí index của giá trị 1 trong list, output: 0
my_list.append(6)        # Thêm phần tử vào cuối list, output: [9, 2, 3, 4, 5, 6]
my_list.insert(1, 0)     # Chèn phần tử 0 vào vị trí index 1, output: [9, 0, 2, 3, 4, 5, 6]
my_list.remove(3)        # Xóa phần tử có giá trị 3 khỏi list, output: [9, 0, 2, 4, 5, 6]
del my_list[-2]        # Xóa phần tử tại vị trí index -2, output: [9, 0, 2, 4, 6]
my_list.pop()          # Xóa và trả về phần tử cuối cùng trong list, output: 6, list còn lại: [9, 0, 2, 4]
my_list.sort()           # Sắp xếp list theo thứ tự tăng dần, output: [0, 2, 4, 9]
my_list.sort(reverse=True)  # Sắp xếp list theo thứ tự giảm dần, output: [9, 4, 2, 0]
my_list.reverse()        # Đảo ngược thứ tự list, output: [0, 2, 4, 9]
my_list.extend([7, 8, 9])  # Mở rộng list bằng cách thêm các phần tử từ một list khác, output: [0, 2, 4, 9, 7, 8, 9]
my_list.count(9)        # Đếm số lần xuất hiện của giá trị 9 trong list, output: 2
len(my_list)           # Lấy độ dài của list output: 8
my_list.clear()          # Xóa tất cả các phần tử trong list, output: []

------------------------------------------------------------------------
# Ví dụ 2
my_list2 = [1, 2, 3, 4, 5]
max(my_list2)        # Tìm giá trị lớn nhất trong list, output: 5
min(my_list2)         # Tìm giá trị nhỏ nhất trong list, output: 1
sum(my_list2)        # Tính tổng các phần tử trong list, output: 15

------------------------------------------------------------------------
# List lồng nhau, truy cập phần tử trong list lồng nhau
"- Ví dụ 1:"
my_list3 = [['Romeo', 15], ['Juliet', 14], ['Mercutio', 16]]
print(my_list3[0][0])   # Output: Romeo , [] đầu tiên là index của list con, [] thứ hai là index của phần tử trong list con
print(my_list3[1][1])   # Output: 14

" - Ví dụ 2:"
matrix = [              # đây là nền tảng của ma trận, ảnh, map,...
  [1,2,3],
  [4,5,6]
]

------------------------------------------------------------------------
# Sao chép list và so sánh list
lst1 = [1, 2, 3]
lst2 = lst1.copy()   # Tạo bản sao của lst1
lst3 = lst2
print(lst2 is lst1)   # Output: False, vì lst2 và lst1 là hai đối tượng khác nhau trong bộ nhớ
print(lst3 is lst1)   # Output: True, vì lst3 tham chiếu đến cùng một đối tượng với lst1
print(lst2 == lst1)   # Output: True, vì lst2 và lst1 có cùng giá trị
print(lst3 == lst1)   # Output: True, vì lst3 và lst1 có cùng giá trị

------------------------------------------------------------------------
# Cắt List (list slicing), a = listname[start:stop:step]
lst4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
newlst4 = lst4[1:4]   # Tạo một list mới từ lst4, bao gồm các phần tử từ index 1 đến index 3, output: [20, 30, 40]
newlst5 = lst4[1:9:2]  # Tạo một list mới từ lst4, bao gồm các phần tử từ index 1 đến index 8, với bước nhảy là 2, output: [20, 40, 60, 80]
newlst6 = lst4[::2]    # Tạo một list mới từ lst4, bao gồm tất cả các phần tử với bước nhảy là 2, output: [10, 30, 50, 70, 90]
newlst7 = lst4[::-2]  # Tạo một list mới từ lst4, bao gồm tất cả các phần tử với bước nhảy là -2 (đảo ngược), output: [100, 80, 60, 40, 20]
newlst8 = lst4[:]      # Tạo một bản sao của lst4, output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
newlst9 = lst4[:9]     # Tạo một list mới từ lst4, bao gồm các phần tử từ đầu đến index 8, output: [10, 20, 30, 40, 50, 60, 70, 80, 90]
newlst10 = lst4[5:]     # Tạo một list mới từ lst4, bao gồm các phần tử từ index 5 đến cuối list, output: [60, 70, 80, 90, 100]
newlst11 = lst4[5::2]  # Tạo một list mới từ lst4, bao gồm các phần tử từ index 5 đến cuối list, với bước nhảy là 2, output: [60, 80, 100]

------------------------------------------------------------------------
# Duyệt list bằng vòng lặp for
for i in lst4:
  print(i)   # Output: 10 20 30 40 50 60 70 80 90 100

------------------------------------------------------------------------
# Duyệt bằng index
for i in range(len(lst4)):            # Duyệt từ 0 đến len(lst4)-1
  print(lst4[i])                      # Output: 10 20 30 40 50 60 70 80 90 100

------------------------------------------------------------------------
# List chứa các kiểu dữ liệu khác nhau
my_list4 = [1, "hello", 3.14, True, [1, 2, 3], (4, 5, 6), {"name": "Alice", "age": 25}]       # chứa số nguyên, chuỗi, số thực, boolean, list, tuple và dictionary


=====================================================================================
=====================================================================================

# BÀI 10: DICTIONARY (DICT) VÀ CÁC PHƯƠNG THỨC THƯỜNG DÙNG VỚI DICTIONARY
"""
- List lưu một tập dữ liệu, Dictionary lưu một đối tượng có nhiều thuộc tính
- Dictionary là một kiểu dữ liệu trong Python dùng để lưu trữ các cặp key-value, trong đó key là khóa duy nhất và value là giá trị tương ứng.
- Dictionary được tạo bằng cách sử dụng dấu ngoặc nhọn {} và các cặp key-value được phân tách bằng dấu hai chấm (:).
- Các key trong dictionary phải là các kiểu dữ liệu không thể thay đổi (immutable), như số, chuỗi, hoặc tuple.
- Dictionary hỗ trợ các phương thức như keys(), values(), items(), get(), update(), pop(), popitem(), clear() và nhiều phương thức khác.
- Dictionary có thể được truy cập bằng key, và có thể sử dụng phương thức get() để truy cập giá trị mà không gây lỗi nếu key không tồn tại.
- Dictionary thường được sử dụng khi cần lưu trữ và truy xuất dữ liệu theo khóa duy nhất, thay vì theo chỉ số như list."""

------------------------------------------------------------------------
# Ví dụ 1: Ta có list:
robot = [
  "AGV",
  0.5,
  80,
  True
]
">> Khi xem lại, ta không biết 0.5 là gì, 80 là gì, True là gì, nên ta sẽ dùng dict để lưu trữ dữ liệu có ý nghĩa hơn:"

robot_dict = {
  "name": "AGV",
  "speed": 0.5,
  "battery": 80,
  "connected": True
}
">> Khi xem lại, ta biết speed là tốc độ, battery là pin, connected là kết nối hay không, nên dict giúp ta lưu trữ dữ liệu có ý nghĩa hơn list."
">> Ở đây, name, speed, battery, connected là key, còn AGV, 0.5, 80, True là value."

------------------------------------------------------------------------
# Lấy giá trị từ dict bằng key
robot_dict["name"]      
print(robot_dict["name"])   # Output: AGV
"hoặc:"
robot_dict.get("speed")  # Output: 0.5
print(robot_dict.get("speed"))  # Output: 0.5

------------------------------------------------------------------------
# Thêm, sửa, xóa giá trị trong dict
robot_dict["battery"] = 90   # Sửa giá trị của key "battery"
robot_dict["color"] = "red"  # Thêm key-value mới vào dict
del robot_dict["connected"]  # Xóa key-value "connected" khỏi dict

------------------------------------------------------------------------
# Duyệt dict bằng vòng lặp for
for key, value in robot_dict.items():
  print(key, value)   # Output: name AGV, speed 0.5, battery 90, color red
  # kiểm tra key
  if key == "battery":
    print("Battery level:", value)   # Output: Battery level: 90

------------------------------------------------------------------------
# Dict lồng nhau, truy cập giá trị trong dict lồng nhau
robot = {
  "motor":{
    "speed":0.5,
    "temperature":40
  },
  "battery":85
}
print(robot["motor"]["speed"])   # Output: 0.5

------------------------------------------------------------------------
# List và dict kết hợp, truy cập giá trị trong list chứa dict
robots = [
  {
    "id":1,
    "battery":90
  },
  {
    "id":2,
    "battery":65
  }
]

------------------------------------------------------------------------
# Dict dùng phương thức get(): để truy cập giá trị, tránh lỗi khi key không tồn tại
robot = {
    "battery": 80,
    "speed": 0.5
}

print(robot.get("battery"))         # Output: 80 

">> Khác với robot[``battery``], nếu key không tồn tại, get() sẽ trả về None thay vì gây lỗi KeyError"

# Có thể đặt giá trị mặc định khi key không tồn tại
print(robot.get("color", "unknown"))  # Output: unknown

-----------------------------------------------------------------------
# Dict dùng phương thức keys(): để lấy danh sách các key trong dict
student = {
  "name": "Quang",
  "age": 23
}
print(student.keys())   # Output: dict_keys(['name', 'age']),  dict_keys là một kiểu dữ liệu đặc biệt của Python, nó giống như một list nhưng không thể thay đổi (immutable) và không hỗ trợ các phương thức của list như append(), remove(), pop()...

------------------------------------------------------------------------
# Dict dùng phương thức values(): để lấy danh sách các value trong dict
print(student.values())   # Output: dict_values(['Quang', 23])

------------------------------------------------------------------------
# Dict dùng phương thức items(): để lấy danh sách các cặp key-value trong dict
print(student.items())   # Output: dict_items([('name', 'Quang'), ('age', 23)])

"- Ví dụ 1: Duyệt dict bằng vòng lặp for"
student = {
  "name": "Quang",
  "age": 23
}
for key, value in student.items():
  print(key, value)                         # Output: name Quang, age 23

------------------------------------------------------------------------
# Dict dùng phương thức update(): để cập nhật value của dict. Phương thức này có thể thêm hoặc sửa nhiều key-value cùng lúc.
"- Ví dụ 1: Cập nhật giá trị của key đã tồn tại"
student.update({"grade": "A"})  # Thêm key-value mới hoặc cập nhật giá trị của key đã tồn tại
print(student)  # Output: {'name': 'Quang', 'age': 23, 'grade': 'A'}

"- Ví dụ 2: Cập nhật nhiều key-value cùng lúc"
student.update({
  "grade": "B",
  "major": "Computer Science"
})
print(student)  # Output: {'name': 'Quang', 'age': 23, 'grade': 'B', 'major': 'Computer Science'}

------------------------------------------------------------------------
# Dict dùng phương thức pop(): để xóa một key-value khỏi dict và trả về giá trị của key đó. Nếu key không tồn tại, sẽ gây lỗi KeyError.
student = {
  "name": "Quang",
  "age": 23
}
grade = student.pop("grade", "Not found")  # Xóa key "grade" và trả về giá trị của nó, nếu key không tồn tại thì trả về "Not found"
print(grade)  # Output: Not found
print(student)  # Output: {'name': 'Quang', 'age': 23}

grade2 = student.pop("age", "Not found")  # Xóa key "age" và trả về giá trị của nó, nếu key không tồn tại thì trả về "Not found"
print(grade2)  # Output: 23
print(student)  # Output: {'name': 'Quang'}

------------------------------------------------------------------------
# Dict dùng phương thức popitem(): để xóa và trả về một cặp key-value cuối cùng (theo thứ tự thêm vào). Nếu dict rỗng, sẽ gây lỗi KeyError.
student = {
  "name": "Quang",
  "age": 23
}
key, value = student.popitem()  # Xóa và trả về một cặp key-value cuối cùng
print(key, value)  # Output: age 23
print(student)  # Output: {'name': 'Quang'} >> đã xóa key "age" khỏi dict, còn lại key "name"

------------------------------------------------------------------------
# Dict dùng phương thức clear(): để xóa tất cả các key-value khỏi dict, dict sẽ trở thành rỗng.
student = {
  "name": "Quang",
  "age": 23
}
student.clear()
print(student)  # Output: {}

------------------------------------------------------------------------
# Dict dùng phương thức copy(): để tạo một bản sao của dict, bản sao này sẽ là một đối tượng mới trong bộ nhớ, không liên kết với dict gốc.
student = {
  "name": "Quang",
  "age": 23
}
student_copy = student.copy()
print(student_copy)  # Output: {'name': 'Quang', 'age': 23}

------------------------------------------------------------------------
# Dict dùng phương thức setdefault(): để lấy giá trị của key nếu tồn tại, nếu không tồn tại thì thêm key với giá trị mặc định và trả về giá trị đó.
student = {
  "name": "Quang",
  "age": 23
}
grade = student.setdefault("grade", "C")      # Nếu key "grade" không tồn tại, thêm key "grade" với giá trị mặc định "C" và trả về giá trị đó
print(grade)  # Output: C
print(student)  # Output: {'name': 'Quang', 'age': 23, 'grade': 'C'}


====================================================================================
=====================================================================================
# BÀI 11. Tuple và các phương thức thường dùng với Tuple
"""
- Tuple khác với list ở chỗ list là kiểu dữ liệu có thể thay đổi (mutable).
- Tuple là kiểu dữ liệu không thể thay đổi (immutable), tức là sau khi tạo, không thể thêm, xóa hoặc thay đổi các phần tử trong tuple.
- Ví dụ như:
  + bảo vệ dữ liệu, tránh bị thay đổi giá trị trong quá trình xử lý. (tọa độ GPS, thông số robot,...)
  + biểu diễn các giá trị cố định, không thay đổi trong suốt chương trình.
- Tuple được tạo bằng cách sử dụng dấu ngoặc đơn ().
- Các phần tử trong tuple có thể là các kiểu dữ liệu khác nhau, bao gồm cả list và tuple khác.
- Tuple hỗ trợ các phương thức như count() và index().
- Tuple thường được sử dụng khi muốn lưu trữ một tập hợp các giá trị mà không cần thay đổi chúng.
- Tuple có hiệu suất nhanh hơn list trong một số trường hợp do tính bất biến của nó.
- Tư duy lập trình:
+ List: Một tập dữ liệu sẽ thay đổi theo thời gian.
+ Một nhóm giá trị luôn đi cùng nhau, không thay đổi theo thời gian
"""

------------------------------------------------------------------------
# Ví dụ 1
my_tuple1 = (1, 2, 3, 4, 5)
my_tuple1[0]      # Truy cập phần tử tại vị trí index 0, output: 1
my_tuple1[-1]    # Truy cập phần tử cuối cùng trong tuple, output: 5
my_tuple1[1] = 9    # Lỗi, vì tuple không thể thay đổi giá trị phần tử
my_tuple1.append(6)   # Lỗi, vì tuple không thể thêm phần tử mới
my_tuple1 += (6, 7)   # Tạo một tuple mới bằng cách nối my_tuple1 với một tuple khác, output: (1, 2, 3, 4, 5, 6, 7)
my_tuple1.index(3)   # Tìm vị trí index của giá trị 3 trong tuple, output: 2
my_tuple1.count(2)   # Đếm số lần xuất hiện của giá trị 2 trong tuple, output: 1
len(my_tuple1)     # Lấy độ dài của tuple, output: 5

------------------------------------------------------------------------
# Ví dụ 2
my_tuple2 = (10, 20, 30, 40, 50)
max(my_tuple2)      # Tìm giá trị lớn nhất trong tuple, output: 50
min(my_tuple2)       # Tìm giá trị nhỏ nhất trong tuple, output: 10
sum(my_tuple2)      # Tính tổng các phần tử trong tuple, output: 150

------------------------------------------------------------------------
# Tuple lồng nhau, truy cập phần tử trong tuple lồng nhau
my_tuple3 = (("Alice", 30), ("Bob", 25), ("Charlie", 35))
print(my_tuple3[0][0])   # Output: Alice
print(my_tuple3[1][1])   # Output: 25     

------------------------------------------------------------------------
# Duyệt tuple bằng vòng lặp for
for i in my_tuple2:
  print(i)   # Output: 10 20 30 40 50

------------------------------------------------------------------------
# Packing và Unpacking tuple
"- Packing: Gói nhiều giá trị vào một tuple"
a = 1
b = 2
c = 3
my_tuple4 = (a, b, c)    # Packing
print(my_tuple4)          # Output: (1, 2, 3)

"- Unpacking: Giải nén các giá trị từ tuple và gán chúng cho các biến"
x, y, z = my_tuple4      # Unpacking
print(x, y, z)           # Output: 1 2 3


====================================================================================
=====================================================================================
# BÀI 12: Set và các phương thức thường dùng với Set
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

------------------------------------------------------------------------
# set() dùng phương thức union(): để hợp hai set lại với nhau, trả về một set mới chứa tất cả các phần tử từ cả hai set, loại bỏ các phần tử trùng lặp.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)  # Hợp set1 và set2
print(set3)  # Output: {1, 2, 3, 4, 5}

------------------------------------------------------------------------
# unique với set()
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)  # Chuyển list thành set để loại bỏ các phần tử trùng lặp
print(unique_set)  # Output: {1, 2, 3, 4, 5}


=====================================================================================
=====================================================================================

#BÀI 12: CÂU LỆNH IF-ELSE
age = 15

if age >=18:
  print("Đủ tuổi")
else:
  print("Chưa đủ tuổi")

------------------------------------------------------------------------
# Với chuỗi
password = input("Password: ")

if password =="123456":
    print("Đăng nhập")
else:
    print("Sai mật khẩu")

------------------------------------------------------------------------
# Với bool
connected = True

if connected:                 # Tương đương với: if connected == True:
    print("Đã kết nối")


=====================================================================================
=====================================================================================
 
# BÀI 13: VÒNG LẶP FOR
"""
- Vòng lặp for:
+ Biết trước số lần lặp
+ Dùng duyệt danh sách...
- Vòng lặp while:
+ Không biết trước số lần lặp
+ Lặp đến khi điều kiện sai
"""

# 13.1:
for i in range(5):        # i chạy từ 0 >> 4 (range(n): tạo các số từ 0 >> n-1)
    print("Hello")

------------------------------------------------------------------------
# 13.2: range(start, stop)
for i in range(3,8):      # i chạy từ 3 >> 7
    print(i)

------------------------------------------------------------------------
# 13.3: range(start, stop, step)
for i in range(0,10,2):   
    print(i)

------------------------------------------------------------------------
# 13.4: Kết hợp for với if
for i in range(6):
  if i % 2 == 0:
    print(i)                # kết quả: 0 2 4

------------------------------------------------------------------------
# 13.5: Vòng lặp Lồng nhau
for i in range(3):
  for j in range(2):
    print(i,j)
"""
- Nghĩa là với mỗi giá trị của i, vòng lặp j sẽ chạy hết một lượt.
- Kết quả:
  0 0
  0 1

  1 0
  1 1

  2 0
  2 1
"""


=====================================================================================
=====================================================================================

# BÀI 14: VÒNG LẶP WHILE
# 14.1: Vòng lặp while cơ bản 
i = 0
while i < 5:
  print(i)
  i = i + 1                 # điều kiện phải thay đổi trong vòng lặp while, nếu không sẽ dẫn đến vòng lặp vô hạn

------------------------------------------------------------------------
# 14.2: While True 
while True:
  password = input("Password: ")          # Điều kiện True luôn đúng, nên vòng lặp sẽ chạy vô hạn. Dùng Ctrl + C để dừng chương trình.
  if password == "123":                  
   break                                  # Dùng break để thoát khỏi vòng lặp while True
  if password != "123":
    continue                              # Dùng continue để bỏ qua các câu lệnh phía dưới và quay lại đầu vòng lặp while True
  
# >> Robot hoạt động gần giống như vậy, nó sẽ tiếp tục thực hiện các hành động (đọc camera -> đọc lidar -> tính toán -> điều khiển motor -> quay lại từ đầu) cho đến khi gặp điều kiện dừng hoặc bị tắt nguồn.

------------------------------------------------------------------------
# 14.3: Vòng lặp while với else
i = 0
while i < 5:
  print(i)
  i = i + 1
else:
  print("Vòng lặp while kết thúc")


=====================================================================================
=====================================================================================

# BÀI 15: HÀM (FUNCTION)
# 15.1: Hàm cơ bản
def greet():                        # Hàm không có tham số (parameters) và không trả về giá trị
    print("Hello, World!")

# Gọi hàm
greet()                            # Output: Hello, World!

------------------------------------------------------------------------
# 15.2: Hàm có tham số
def greet2(name):                   # Hàm có tham số name
    print(f"Hello, {name}!")        # thêm f-string để nhúng giá trị biến name vào chuỗi, có thể chèn biến ở bất kỳ vị trí nào trong chuỗi, miễn là đặt trong dấu ngoặc nhọn {}
    print("Hello", name)            # Chỉ truyền các đối số cho print(), muốn thêm dấu câu phải tách riêng hoặc ghép chuỗi, đơn giản phù hợp khi chỉ in nhiều giá trị

------------------------------------------------------------------------
# Gọi hàm với tham số
greet2("Alice")                    # Output: Hello, Alice!
                                  # Alice được gọi là đối số (argument) truyền vào hàm greet2, còn name là tham số (parameter) của hàm greet2, khi gọi hàm, giá trị của đối số sẽ được gán cho tham số tương ứng.

------------------------------------------------------------------------
#15.3 Return trong hàm
def add(a, b):                      # Hàm có tham số a và b
    return a + b                    # Trả về tổng của a và b
                                    # nếu dùng print() trong hàm thì sẽ in ra giá trị nhưng không trả về giá trị, ví dụ x = add(5, 3) thì print(x) sẽ trả về None còn return sẽ trả về giá trị là 8, nên khi muốn sử dụng giá trị trả về của hàm thì phải dùng return, còn print() chỉ để hiển thị giá trị ra màn hình.


=====================================================================================
=====================================================================================
# BÀI 16: Exception (Xử lý ngoại lệ)
"""
- Exception là một cơ chế trong Python để xử lý các lỗi xảy ra trong quá trình thực thi chương trình.
- Khi một lỗi xảy ra, Python sẽ tạo ra một đối tượng Exception và dừng chương trình. Nếu không xử lý ngoại lệ, chương trình sẽ bị dừng và hiển thị thông báo lỗi.
- Để xử lý ngoại lệ, ta sử dụng khối try-except. Trong khối try, ta đặt các câu lệnh có thể gây ra lỗi. Nếu một lỗi xảy ra, Python sẽ nhảy đến khối except và thực hiện các câu lệnh trong đó.
- Ta có thể sử dụng nhiều khối except để xử lý các loại lỗi khác nhau, hoặc sử dụng except Exception để xử lý tất cả các loại lỗi.
- Ngoài ra, ta có thể sử dụng khối finally để thực hiện các câu lệnh cuối cùng, bất kể có lỗi xảy ra hay không.
- Ta cũng có thể sử dụng raise để tạo ra một ngoại lệ tùy chỉnh
"""

#16.1. Xử lý lỗi chia cho 0
print("Bắt đầu")
number = int(input("Nhập số: "))          # Nếu người dùng nhập vào một giá trị không phải là số nguyên, sẽ gây ra lỗi ValueError
print("Kết thúc")

"- Cách xử lý: try-except (nếu try có lỗi thì sẽ nhảy sang except, nếu không có lỗi thì sẽ bỏ qua except và tiếp tục thực hiện các câu lệnh phía dưới)"
try:
  number = int(input("Nhập số: "))
  print("Kết thúc")
except ValueError:                              # Chỉ bắt lỗi ValueError, nếu để mỗi except: thì sẽ bắt tất cả các lỗi, nhưng không biết lỗi gì, nên chỉ bắt lỗi cụ thể để dễ dàng xử lý         
  print("Lỗi: Vui lòng nhập một số nguyên.")

------------------------------------------------------------------------
#16.2. Xử lý lỗi chia cho 0
try:
  x = 10/0
except ZeroDivisionError:
  print("Không chia được cho 0")

------------------------------------------------------------------------
#16.3. Xử lý nhiều loại lỗi
try:
  number = int(input())
  result = 10 / number

except ValueError:
  print("Không phải số")

except ZeroDivisionError:
  print("Không chia được cho 0")

------------------------------------------------------------------------
#16.4. Sử dụng với else:
try:
  number = int(input())

except ValueError:
  print("Sai")

else:                      # nếu không lỗi chạy else
  print("Đúng")

------------------------------------------------------------------------
#16.5. Sử dụng với finally:
try:
  print("Mở camera")

except:
  print("Có lỗi")

finally:
  print("Đóng camera")               # dù có lỗi hay không thì vẫn chạy finally, ví dụ như đóng camera, tắt kết nối, giải phóng tài nguyên,...

------------------------------------------------------------------------
#16.6. Sử dụng raise để tạo ra một ngoại lệ tùy chỉnh
def check_positive(number):
  if number < 0:
    raise ValueError("Số phải là số dương")   # Tạo ra một ngoại lệ ValueError với thông báo tùy chỉnh và tìm nơi nào đang try -except để xử lý ngoại lệ này
  else:
    print("Số hợp lệ:", number) 

number = int(input("Nhập một số: "))
try:
  check_positive(number)                      # Gọi hàm check_positive() để kiểm tra số nhập vào, nếu số âm thì sẽ raise ValueError và nhảy sang except để xử lý lỗi
except ValueError as e:                       # Bắt ngoại lệ ValueError và gán vào biến e
  print("Lỗi:", e)


=====================================================================================
=====================================================================================
# BÀI 17: Đọc và ghi tệp 
# 17.1. Mở file
file = open("example.txt", "r")   # Mở file example.txt ở chế độ đọc (read)
file = open("example.txt", "w")   # Mở file example.txt ở chế độ ghi (write), nếu file không tồn tại thì sẽ tạo mới, nếu file tồn tại thì sẽ xóa nội dung cũ và ghi đè nội dung mới
file = open("example.txt", "a")   # Mở file example.txt ở chế độ ghi (append), nếu file không tồn tại thì sẽ tạo mới, nếu file tồn tại thì sẽ ghi thêm nội dung mới vào cuối file mà không xóa nội dung cũ
file = open("example.txt", "r+")  # Mở file example.txt ở chế độ đọc và ghi (read and write), nếu file không tồn tại thì sẽ tạo mới, nếu file tồn tại thì sẽ đọc và ghi nội dung mới vào file mà không xóa nội dung cũ

------------------------------------------------------------------------
# 17.2. Mở file với with (tự động đóng file sau khi thực hiện xong)
with open("data.txt", "r") as file:  # Mở file data.txt ở chế độ đọc (read) và gán cho biến file, sau khi thoát khỏi khối with thì file sẽ tự động đóng
  content = file.read()
  print(content)                # Output: nội dung của file data.txt

------------------------------------------------------------------------
# 17.3. Đọc file  
file = open("data.txt", "r")  # Mở file data.txt ở chế độ đọc (read)
content = file.read()
print(content)                # Output: nội dung của file data.txt
file.close()                  # Đóng file sau khi đọc xong để giải phóng tài nguyên, tránh lỗi "too many open files"

------------------------------------------------------------------------
# 17.4. Đọc file theo từng dòng
with open("data.txt") as file:
  for line in file:                  
    print(line)

------------------------------------------------------------------------
# 17.5. Đọc 1 dòng trong file
with open("data.txt") as file:
  line = file.readline()          # Đọc 1 dòng trong file data.txt
  print(line)                     # Output: dòng đầu tiên của file data.txt

------------------------------------------------------------------------
# 17.6. Đọc tất cả các dòng trong file và lưu vào list
with open("data.txt") as file:
  lines = file.readlines()        # Đọc tất cả các dòng trong file data.txt và lưu vào list
  print(lines)                    # Output: danh sách các dòng trong file data.txt thành các phần tử của list, mỗi phần tử là một dòng trong file data.txt

------------------------------------------------------------------------
# 17.7. Ghi file
file = open("data.txt", "w")  # Mở file data.txt ở chế độ ghi (write)
file.write("Hello, World!")   # Ghi chuỗi "Hello, World!" vào file data.txt, nếu file đã có nội dung thì sẽ bị ghi đè
file.close()                  # Đóng file sau khi ghi xong để giải phóng tài nguyên

------------------------------------------------------------------------
# 17.8. Ghi file với append (thêm vào cuối file)
file = open("data.txt", "a")  # Mở file data.txt ở chế độ ghi (append)
file.write("\nHello again!")   # Ghi chuỗi "Hello again!" vào cuối file data.txt, nếu file đã có nội dung thì sẽ không bị ghi đè
file.close()                  # Đóng file sau khi ghi xong để giải phóng tài nguyên

------------------------------------------------------------------------
# 17.9. Ghi nhiều dòng vào file
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("data.txt", "w") as file:
  file.writelines(lines_to_write)  # Ghi nhiều dòng vào file data.txt, mỗi phần tử của list là một dòng trong file data.txt

------------------------------------------------------------------------
# 17.10. Đọc file an toàn với try-except
try:
  with open("abc.txt") as file:
    print(file.read())

except FileNotFoundError:                 # Nếu file không tồn tại thì sẽ bắt lỗi FileNotFoundError và thực hiện các câu lệnh trong except
  print("Không tìm thấy file")

------------------------------------------------------------------------
# 17.11. Đọc file CSV
import csv
with open("data.csv", newline='') as csvfile:  # Mở file data.csv ở chế độ đọc (read) và gán cho biến csvfile, newline='' để tránh lỗi khi đọc file CSV trên Windows
    reader = csv.reader(csvfile)                # Tạo một đối tượng reader để đọc file CSV
    for row in reader:                          # Duyệt từng dòng trong file CSV
        print(row)                              # Output: danh sách các giá trị trong mỗi dòng của file CSV, mỗi giá trị được phân tách bằng dấu phẩy
 

=====================================================================================
=====================================================================================
# BÀI 18: Lập trình hướng đối tượng (OOP)
"""
- Lập trình hướng đối tượng (Object-Oriented Programming - OOP) là một phương pháp lập trình dựa trên khái niệm "đối tượng" (object), trong đó các đối tượng có thể chứa dữ liệu (thuộc tính) và các phương thức (hàm) để thao tác với dữ liệu đó.
- Các khái niệm cơ bản trong OOP:
+ Class (Lớp): Là một khuôn mẫu (template) để tạo ra các đối tượng. Class định nghĩa các thuộc tính và phương thức mà các đối tượng của nó sẽ có.
+ Object (Đối tượng): Là một thực thể cụ thể được tạo ra từ một class. Mỗi object có thể có các giá trị riêng cho các thuộc tính của nó.
+ Attribute (Thuộc tính): Là các biến được định nghĩa trong class, dùng để lưu trữ dữ liệu của đối tượng.
+ Method (Phương thức): Là các hàm được định nghĩa trong class, dùng để thực hiện các hành động hoặc thao tác trên dữ liệu của đối tượng.
- Các tính chất của OOP: 
+ Tính đóng gói (Encapsulation): Là khả năng ẩn đi các chi tiết bên trong của một đối tượng và chỉ cho phép truy cập thông qua các phương thức công khai.
+ Tính kế thừa (Inheritance): Là khả năng tạo ra một class mới dựa trên một class đã tồn tại, cho phép tái sử dụng mã nguồn và mở rộng chức năng.
+ Tính đa hình (Polymorphism): Là khả năng sử dụng cùng một phương thức trên các đối tượng khác nhau, cho phép các đối tượng có thể được xử lý theo cách giống nhau mặc dù chúng có thể có các hành vi khác nhau.
+ Tính trừu tượng (Abstraction): Là khả năng tập trung vào các đặc điểm quan trọng của một đối tượng và bỏ qua các chi tiết không cần thiết, giúp giảm độ phức tạp và tăng tính linh hoạt trong lập trình.
 """

# 18.1. Tạo class và object
class Robot:                       # Tạo class Robot
    def __init__(self, name2, speed2):  # Hàm khởi tạo (constructor) __init__ của class Robot, được gọi khi tạo một object mới từ class Robot, self là tham số đại diện cho object hiện tại, name2 và speed2 là các tham số được truyền vào khi tạo object
        self.name = name2              # Thuộc tính name của object được gán giá trị từ tham số name2
        self.speed = speed2            # Thuộc tính speed của object được gán giá trị từ tham số speed2

    def move(self):                   # Phương thức (method) move của class Robot
        print(f"{self.name} is moving at {self.speed} m/s")  # In ra thông tin về robot đang di chuyển

robot1 = Robot("R2D2", 5)  # Tạo object robot1 từ class Robot
robot1.move()  # Gọi phương thức move của object robot1, Output: R2D2 is moving at 5 m/s

------------------------------------------------------------------------
#18.2. Tham số mặc định trong hàm khởi tạo
class Robot2:
    def __init__(self, name2="Robot", speed2=1):  # Tham số mặc định name2="Robot" và speed2=1, nếu không truyền giá trị khi tạo object thì sẽ sử dụng giá trị mặc định
        self.name = name2
        self.speed = speed2

    def move(self):
        print(f"{self.name} is moving at {self.speed} m/s")

robot2 = Robot2()  # Tạo object robot2 từ class Robot2 mà không truyền giá trị, sẽ sử dụng giá trị mặc định
robot2.move()  # Output: Robot is moving at 1 m/s

------------------------------------------------------------------------
# 18.3. Mutable và Immutable trong OOP
"""
- Trong lập trình hướng đối tượng (OOP), mutable và immutable là hai khái niệm quan trọng liên quan đến khả năng thay đổi trạng thái của các đối tượng.
- Mutable (có thể thay đổi): Là các đối tượng có thể thay đổi trạng thái hoặc giá trị của chúng sau khi được tạo ra. Ví dụ: list, dict, set trong Python là các kiểu dữ liệu mutable. Khi bạn thay đổi một phần tử trong list, dict hoặc set, bạn đang thay đổi trạng thái của đối tượng đó.
- Immutable (không thể thay đổi): Là các đối tượng không thể thay đổi trạng thái hoặc giá trị của chúng sau khi được tạo ra. Ví dụ: tuple, str, int, float trong Python là các kiểu dữ liệu immutable. Khi bạn cố gắng thay đổi một phần tử trong tuple hoặc str, bạn sẽ nhận được lỗi hoặc tạo ra một đối tượng mới thay vì thay đổi đối tượng ban đầu.
- Trong OOP, việc hiểu rõ mutable và immutable giúp lập trình viên quản lý bộ nhớ hiệu quả hơn, tránh các lỗi không mong muốn và thiết kế các lớp (class) và đối tượng (object) một cách hợp lý.
- Những đối tượng mutable như list, dict, set thường được sử dụng khi cần lưu trữ và thay đổi dữ liệu trong quá trình thực thi chương trình. Trong khi đó, những đối tượng immutable như tuple, str, int, float thường được sử dụng khi cần bảo vệ dữ liệu khỏi bị thay đổi hoặc khi muốn đảm bảo tính toàn vẹn của dữ liệu.
"""

------------------------------------------------------------------------
# 18.4. Composition (Tổng hợp) trong OOP
"""
- Quan hệ giữa 2 class là "HAS-A" (vd: Robot has-a Battery)
- Composition (Tổng hợp) là một khái niệm trong lập trình hướng đối tượng (OOP) mà trong đó một đối tượng được tạo thành từ các đối tượng khác. Nó cho phép xây dựng các đối tượng phức tạp bằng cách kết hợp các đối tượng đơn giản hơn.
- Composition giúp tăng tính linh hoạt và khả năng tái sử dụng mã nguồn, vì các đối tượng có thể được kết hợp theo nhiều cách khác nhau để tạo ra các đối tượng mới mà không cần phải kế thừa từ một lớp cơ sở.
- Ví dụ: Một robot có thể được tạo thành từ các bộ phận như động cơ, cảm biến, và bộ điều khiển. Mỗi bộ phận này có thể được triển khai như một đối tượng riêng biệt, và robot sẽ tổng hợp các đối tượng này để thực hiện các chức năng của nó. 
"""

"- Ví dụ 1:"
class Motor:

    def __init__(self):

        self.speed = 0

    def set_speed(self, speed):

        self.speed = speed

class Robot:

    def __init__(self):

        self.left_motor = Motor()                 # Tạo self.left_motor là một đối tượng của class Motor, tức là Robot có một Motor bên trong nó, đây là ví dụ về Composition (Tổng hợp) trong OOP

        self.right_motor = Motor()

    def move_forward(self):

        self.left_motor.set_speed(50)             # Vì self.left_motor là một đối tượng của class Motor, nên có thể gọi phương thức set_speed() của class Motor thông qua self.left_motor

        self.right_motor.set_speed(50)

------------------------------------------------------------------------
"- Ví dụ 2:"
class Battery:

    def __init__(self):
        self.level = 100

    def discharge(self, amount):
        self.level -= amount
        if self.level < 0:
            self.level = 0


class Motor:

    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed


class Robot:

    def __init__(self, name):
        self.name = name
        self.battery = Battery()
        self.left_motor = Motor()
        self.right_motor = Motor()

    def move_forward(self):
        self.left_motor.set_speed(50)
        self.right_motor.set_speed(50)
        self.battery.discharge(10)

    def show_info(self):
        print("Tên robot:", self.name)
        print("Pin:", self.battery.level)
        print("Motor trái:", self.left_motor.speed)
        print("Motor phải:", self.right_motor.speed)

robot = Robot("AMR-01")               # output: Tên robot: AMR-01, Pin: 90 , Motor trái: 50, Motor phải: 50

robot.move_forward()                  # nếu không gọi robot.move_forward() thì pin vẫn là 100, motor trái và phải vẫn là 0, vì chưa truyền lệnh set_speed() và discharge() để thay đổi giá trị của các thuộc tính trong class Battery và Motor

robot.show_info()                     # nếu không gọi robot.show_info() thì sẽ không in ra thông tin của robot, vì chưa gọi phương thức show_info() để in ra các thuộc tính của robot

------------------------------------------------------------------------
# 18.5. Kế thừa
"- Quan hệ giữa 2 class là IS-A (vd: AMR is-a Robot)"
# Ví dụ 1
class Robot:
  def move(self):
      print("Robot đang di chuyển")

class AMR(Robot):                           # class AMR kế thừa clas Robot
  pass                                      # pass nghĩa là chưa thêm gì vào class này

robot = AMR()
robot.move()                                # output: Robot đang di chuyển

------------------------------------------------------------------------
# Ví dụ 2: Method Overriding
class Robot:

    def stop(self):
        print("Robot dừng")

class AMR(Robot):

    def stop(self):
        print("AMR phanh")

robot.stop()           # output: AMR phanh   >> sử dụng method riêng, ghi đè lên method của class cha

------------------------------------------------------------------------
# Ví dụ 3
class Robot:

    def __init__(self, name):
        self.name = name

    def move(self,sp):
        self.sp = sp


class AMR(Robot):

    def __init__(self, name, max_speed,sp2):

        super().__init__(name)
        super().move(sp2)
        self.max_speed = max_speed

robot = AMR("AMR-01", 2.0, 600) 
print(robot.name)                   # output: AMR-01
print(robot.max_speed)              # output:2.0
print(robot.sp)                     # output: 600
robot.move(800)
print(robot.sp)                     # output: 800

------------------------------------------------------------------------
# 18.5. Đa hình (Polymorphism)
"- Ví dụ 1:"
class Robot:

    def move(self):
        print("Robot đang di chuyển")

class AMR(Robot):

    def move(self):                                     #AMR và Drone đều override move().
        print("AMR đang chạy trên mặt đất")

class Drone(Robot):

    def move(self):
        print("Drone đang bay")

amr = AMR()                   # tạo object 
drone = Drone()
amr.move()                    # output: AMR đang chạy trên mặt đất           
drone.move()                  # output: Drone đang bay
                              # >> Đều cùng tên method nhưng hành vi khác nhau >> Tính đa hình

------------------------------------------------------------------------
"- Ví dụ 2:"
robots = [              
  AMR(),
  Drone()
]

for robot in robots:
  robot.move()                # output: AMR đang chạy trên mặt đất        Drone đang bay
                              # Chúng ta chỉ viết: robot.move() >> Python tự quyết định phải gọi move() của class nào. Đây chính là Polymorphism.

------------------------------------------------------------------------ 
# 18.6. Property
"""
- Property là một tính năng trong Python cho phép bạn định nghĩa các phương thức (methods) trong class nhưng có thể truy cập chúng như các thuộc tính (attributes)
của đối tượng. Điều này giúp bạn kiểm soát việc truy cập và thay đổi giá trị của các thuộc tính trong class mà vẫn giữ được cú pháp đơn giản và trực quan.
- Getter: Dùng để lấy dữ liệu (vd: robot.battery)
- Setter: Dùng để thay đổi dữ liệu (vd: robot.battery = 80)
"""
class Robot:

    def __init__(self):
        self._speed = 0           # ghi dữ liệu vào object, nếu tạo trùng @property thì sẽ gọi đến setter và check giá trị khởi tạo luôn, nếu không trùng property thì sẽ tạo ra một attribute mới trong object và không gọi setter

    @property                     # Dùng để định nghĩa một phương thức getter, cho phép truy cập giá trị của thuộc tính speed như một thuộc tính thông thường (không cần gọi method)
    def speed(self):              # Coi như một attribute, không cần gọi method, nhưng vẫn có thể kiểm tra giá trị trước khi trả về
        return self._speed        # Láy giá trị và trả về 

    @speed.setter                 # Dùng để định nghĩa một phương thức setter, cho phép thay đổi giá trị của thuộc tính speed như một thuộc tính thông thường (không cần gọi method)
    def speed(self, value):       # khi gán giá trị cho robot.speed = value thì sẽ gọi đến setter và kiểm tra giá trị trước khi gán vào attribute _speed

        if value < 0:
            raise ValueError("Speed không được âm")

        if value > 2.0:
            raise ValueError("Speed vượt quá giới hạn")

        self._speed = value        # nếu thỏa mãn điều kiện thì gán giá trị cho attribute _speed              

robot = Robot()            
robot.speed = 1.5                 # Property cho phép gọi method speed như một attribute (không cần robot.speed() )  >> Gọi Setter
robot.speed = 3.0                 # Gây ra lỗi ValueError: Speed vượt quá giới hạn

------------------------------------------------------------------------ 
# 18.7. Classmethod và Staticmethod
"""
- 
"""














































































































































        