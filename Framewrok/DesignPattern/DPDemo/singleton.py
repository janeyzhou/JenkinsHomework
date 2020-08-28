class Singleton(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


if __name__ == "__main__":
    t1 = Singleton()
    t2 = Singleton()
    print(t1)
    print(t2)
    print(id(t1) == id(t2))
