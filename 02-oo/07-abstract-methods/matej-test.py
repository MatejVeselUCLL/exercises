from abc import ABC, abstractmethod

class A:
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
    

class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()

    # @abstractmethod
    # def a(self):
    #     ...
    
    # @abstractmethod
    # def e(self):
    #     ...

a = A()

