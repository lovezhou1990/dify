
class Class1:
    def method1(self):
        print("Class1 method1")
    @classmethod
    def method2(self):
        print("Class1 method2")

if __name__ == '__main__':
    c1 = Class1()
    c1.method1()
    c1.method2()
    Class1.method2()
    Class1.method1()