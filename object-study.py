class Dog:
    #コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, new_age):
        if new_age >= 0:
            self.age = new_age
        else:
            print("年齢は０以上でなければなりません")

    def bark(self):
        print(f"{self.name}がワン！と鳴いた")

    def introduce(self):
        print(f"私の名前は{self.name}です。{self.age}歳です")

class GuideDog(Dog):
    def guide(self):
        print(f"{self.name}が道案内しています")


my_dog = Dog("ポチ", 3)

my_dog.bark()

dog1.introduce()
dog2.introduce()


class Bird:
    def speak(self):
        print("ピヨ！")

class Cow:
    def speak(self):
        print("モ〜！")

animals = [Bird(), Cow()]

for animal in animals:
    animal.speak()


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width*self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14*self.radius**2)

areas = [Rectangle(3, 4), Circle(3)]

for a in areas:
    a.area()

