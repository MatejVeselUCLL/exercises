from abc import ABC, abstractmethod

# D1 = {a, c}
# C = {b, c}
# D2 = {a, b, c, e}
class A(ABC):
    def a(self):
        self.b()

    def e(self):
        self.c()

    @abstractmethod
    def b(self):
        ...
    
    @abstractmethod
    def c(self):
        ...

# D1 = {a, b, c, e}
# C = {a, e}
class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()

# D1 = {a, b, c, e, f}
# C = {}
class C(B):
    def f(self):
        pass

# D1 = {a, b, c, e}
# C = {f}
# D2 = {a, b, c, e, f}
    
class D(A):
    def b(self):
        self.f()
    
    @abstractmethod
    def f(self):
        ...

# D1 = {a, b, c, e, f, g}
# C = {a, e, f}
class E(D):
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()

# D1 = {a}
# C = {b, f}
class F:
    def a(self):
        self.b()
        self.f()
    
    @abstractmethod
    def b(self):
        ...
    
    @abstractmethod
    def f(self):
        ...

# Opposite of abstract is specific.
