from abc import ABC, abstractmethod

# Set D contains all methods that the class DEFINES or INHERITS.
# Set C contains all methods that the class CALLS.

# D = {a, e}
# C = {b, c}
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


# D = {a, e} + {b, c}
# C = {a, e}
class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()

# D = {a, e, b, c} + {f}
# C = {}
class C(B):
    def f(self):
        pass

# D = {a, e} + {b}
# C = {f}
class D(A):
    def b(self):
        self.f()
    
    @abstractmethod
    def f(self):
        ...

# D = {a, e, b} + {c, f, g}
# C = {a, e, f}
class E(D):
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()


# D = {a}
# C = {b, f}
class F(ABC):
    def a(self):
        self.b()
        self.f()
    
    @abstractmethod
    def b(self):
        ...

    @abstractmethod
    def f(self):
        ...
