#1
class rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width=width
        self.height=height

    def area_calc(self):
        area = self.width*self.height
        print('area: ', area)


    def peri_calc(self):
        perimeter = (self.width*self.height)*2
        print('perimeter: ', perimeter)

print("Calculate area and perimeter of rectangle")
w=int(input('enter width: '))
h=int(input('enter height: '))
rect=rectangle(w,h)
rect.area_calc()
rect.peri_calc()