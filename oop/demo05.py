
"""装饰器实现描述器"""


class Descriptor:

    def __init__(self, name=None, **opt):
        self.name = name
        for key, value in opt.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)
    super_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError()
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


def Unsigned(cls):
    super_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError()
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


def MaxSized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opt):
        if 'size' not in opt:
            raise TypeError()
        super_init(self, name, **opt)

    cls.__init__ = __init__

    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError()
        super_set(self, instance, value)

    cls.__set__ = __set__

    return cls


@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass


def typeassert(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate


@typeassert(name=SizedString(size=5),
            shares=UnsignedInteger,
            price=UnsignedInteger)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('wuyao', 10, 10)
    print(s.shares)
    s.shares = -10
