class A:
    def __init__(self):
        pass

    def get_a(self):
        print('instance method')

    @classmethod
    def get_b(cls):
        print('class method')

    @staticmethod
    def get_c():
        print('static method')

if __name__ == "__main__":
    print(A.get_c)
    print(A.get_b)
    a = A()
    print(a.get_a)
    print(a.get_b)

