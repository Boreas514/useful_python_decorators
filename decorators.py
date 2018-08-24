import functools
import time
import random


def timer(func):
    '''Print the runtime of the decorated function'''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')
        return value
    return wrapper_timer


def debug(func):
    '''Print the function signature and return value'''
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value!r}')
        return value
    return wrapper_debug


def slow_down(func):
    '''Sleep 1 second before calling the function'''
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


PLUGINS = dict()
def register(func):
    '''Register a function as a plug-in'''
    PLUGINS[func.__name__] = func
    return func


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        '''Get value of radius'''
        return self._radius

    @radius.setter
    def radius(self, value):
        '''Set radius, raise error if negative'''
        if value >= 0:
            self._radius = value
        else:
            raise ValueError('Radius must be positive')

    @property
    def area(self):
        '''Calculate area inside circle'''
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        '''Calculate volume of cylinder with circle as base'''
        return self.area * height

    @classmethod
    def unit_circle(cls):
        '''Factory method creating a circle with radius 1'''
        return cls(1)

    @staticmethod
    def pi():
        '''Value of π, could use math.pi instead though'''
        return 3.1415926535


def repeat(num_times):
    '''Repeat execute innerfunction for your choice num'''
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

