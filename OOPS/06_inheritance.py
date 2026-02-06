class BaseChai:
    def __init__(self, type_):
        self.type = type_
    def prepare (self):
        print (f"Preparing {self.type} Chai......")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Add cardmom, Ginger, Cloves.")

class ChaiShop:
    chai_cls =  BaseChai # if i am inheriting all the values of this basechai  we dont use parentheses as "BaseChai()"
    chai_cls.prepare()
    def __init__(self):
        self.chai =self.chai_cls("Regular")
    def serve(self):
        print(f"Severving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

Shop = ChaiShop()
fancy = FancyChaiShop()
Shop.serve()
fancy.serve()
fancy.chai.add_spices()
