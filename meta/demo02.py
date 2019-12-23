from inspect import signature
import logging


"""通过元类检查子类重载方法的签名"""

class MatchSignatureMeta(type):

    def __init__(cls, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(cls, cls)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                pass
            pre_def = getattr(sup, name, None)
            if pre_def:
                pre_sign = signature(pre_def)
                val_sign = signature(value)
                if pre_sign != val_sign:
                    logging.warning('Signature mismatch in %s. %s != %s', value.__qualname__, pre_sign, val_sign)


class Root(metaclass=MatchSignatureMeta):

    def foo(self, x, y, z=10):
        pass



class Bar(Root):

    def foo(self, x, y, h=10):
        pass


if __name__ == '__main__':
    bar = Bar()