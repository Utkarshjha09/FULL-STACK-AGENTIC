class TeaLeaf:
    def __init__(self, age):
        self._age=age

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self,age):
        if 1<= age<=5:
            self.age = age
        else:
            raise ValueError("Tea leaf age must be between 1 to 5")
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age=6
print(leaf.age)    
