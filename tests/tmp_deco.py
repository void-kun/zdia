
class C:
    @decorator
    def f(self):
        pass

class D:
    @factory(arg)
    def g(self):
        pass

class E:
    @module.staticmethod
    def h():
        pass
