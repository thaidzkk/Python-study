class Robot:

    def __init__(self):
        self.xspeed = 1.5           # ghi dữ liệu vào object, nếu tạo trùng property thì sẽ gọi đến setter, nếu không trùng property thì sẽ tạo ra một attribute mới trong object

    @property                     # Dùng để định nghĩa một phương thức getter, cho phép truy cập giá trị của thuộc tính speed như một thuộc tính thông thường (không cần gọi method)
    def xspeed(self):             # Coi như một attribute, không cần gọi method
        return self._speed        # Láy giá trị và trả về 

    @xspeed.setter                 # Dùng để định nghĩa một phương thức setter, cho phép thay đổi giá trị của thuộc tính speed như một thuộc tính thông thường (không cần gọi method)
    def xspeed(self, value):

        if value < 1:
            raise ValueError("Speed không được âm")

        if value > 2.0:
            raise ValueError("Speed vượt quá giới hạn")

        self._speed = value                                     

robot = Robot()            
robot.xspeed = 1.5
print(robot.xspeed)                 # Property cho phép gọi method speed như một attribute (không cần robot.speed() )  >> Gọi Setter







