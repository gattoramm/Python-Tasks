"""Возврат начапьных атрибутов с помощью
декоратора update_wrapper"""
import functools


def is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f (*args, **kwargs)
    return wrapper


def foobar(username='someone'):
    """Do crazy stuff."""
    pass


print(foobar.__doc__)
print(foobar.__name__)
print()


@is_admin
def foobar(username='someone'):
    """Do crazy stuff."""
    pass


print(foobar.__doc__)
print(foobar.__name__)
print()


def foobar2(username='someone'):
    """Do crazy stuff."""
    pass


foobar2 = functools.update_wrapper(is_admin, foobar2)
print(foobar2.__name__)
print(foobar2.__doc__)