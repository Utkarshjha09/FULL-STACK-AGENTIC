class A: #Base Class
    label ="A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A): # this is the way How  we can inherit functions from a classes
    label ="C: Herbal blend"

class  D(B,C):  # this is the way How  we can inherit functions from more than two classes
    pass 


cup =D()
print(cup.label)
print(D.__mro__)