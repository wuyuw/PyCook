
"""描述器"""


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError()
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Integer2:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]


class Point:
    x = 1
    y = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2:
    x = Integer('x')
    y = Integer('y')
    z = Integer2('z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Point3:

    def __init__(self, x, y):
        self.x = Integer('x')
        self.y = Integer('y')
        self.x = x
        self.y = y


class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return instance
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError()
        self.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate


@typeassert(name=str, price=float)
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price


if __name__ == '__main__':
    p = Point(3, 4)
    print(p.x)
    p.x = 5
    print(p.x)

    p2 = Point2(3, 4, 5)
    print(p2.x)
    print(p2.x)
    print(p2.z)
    print(p2.z)
    # p2.x = 'a'

    p3 = Point3(5, 6)

    s = Stock('aaa', 1.23)
    s2 = Stock('aaa', 3) # error
