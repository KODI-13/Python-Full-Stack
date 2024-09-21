# Inheritance Realted program
# Operation on polygon 

class polygon:
    def __init__(self,no_side):
        self.no_side = no_side
        self.length = []
    def input_length(self):
        self.length = []
        for i in range(self.no_side):
            s = eval(input(f"Enter side {i+1} : "))
            self.length.append(s)
            # print(self.length)
    def display(self):
        for i in range(len(self.length)):
            print(f"The length of side {i+1} is {self.length[i]}")

pentagon = polygon(5)
pentagon.input_length()
pentagon.display()

# hexagon = polygon(6)
# hexagon.input_length()

class Perimeter_Triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)        # Calling Parent constructor in child class
    def perimeter(self):
        s1,s2,s3 = self.length
        p = s1 + s2 + s3
        print("perimeter of triangle is", p)

t1 = Perimeter_Triangle()
t1.input_length()
t1.display()
t1.perimeter()