class Base(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    t1 = Base()
    t2 = Base()
    print(t1)
    print(t2)
    print(id(t1) == id(t2))
