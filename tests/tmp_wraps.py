
from functools import wraps as rw
from functools import wraps
import functools as ft

class C:
    @wraps
    def f(self):
        pass

class D:
    @rw
    def g(self):
        pass

class E:
    @ft.wraps
    def h(self):
        pass

class F:
    @wraps(original)
    def k(self):
        pass
