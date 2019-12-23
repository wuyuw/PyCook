from functools import wraps
from inspect import signature

# 类型检查
def typeassert(*ty_args, **ty_kwargs):

    def decorate(func):
        sign = signature(func)
        type_values = sign.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            real_values = sign.bind(*args, **kwargs).arguments
            for key, value in real_values.items():
                if key in type_values:
                    if not isinstance(value, type_values[key]):
                        raise TypeError(f'参数{key}类型错误，接收{type_values[key]}, 传入{type(value)}')
            return func(*args, **kwargs)

        return wrapper

    return decorate


@typeassert(int, z=str)
def foo(x, y, z):
    print(x, y, z)


if __name__ == '__main__':
    foo(1, 2, 'hello')
