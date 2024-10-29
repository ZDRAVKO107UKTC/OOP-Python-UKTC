class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_volume(self):
        return self.length * self.width * self.height

box01 = Box(40, 50, 100)
box02  = Box(10, 50, 100)

volume_of_box01 = box01.calculate_volume()
volume_of_box02 = box02.calculate_volume()

print(volume_of_box01)
print(volume_of_box02)