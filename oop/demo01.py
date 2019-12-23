"""访问控制"""

class Person:

    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError()
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError()


if __name__ == '__main__':
    one = Person('wyw')
    print(one.first_name)
    one.first_name = '515'
    print(one.first_name)
    print(one._first_name)

    del one.first_name
