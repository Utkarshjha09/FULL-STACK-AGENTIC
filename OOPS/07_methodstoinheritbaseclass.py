# There are  3 methods of inheriting  1) Code Duplication 2)Explicit call"
# 3) super()
class Chai:
    def __init__(self,type_,strength):
        self.type = type_
        self.strength= strength

## This is Code Duplication method  for inheriting from base class   ##
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        self.strength=strength
        self.type =type_
        self.spice_level=spice_level
# yaha par saari properties ko "Self." se variable mai declare karte hai base class ki v properties ko v 
## This is method for explicitly calling or inheriting from the base class like here is "Chai" we inherit the properties of chai
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
         Chai.__init__(self, type_, strength)
         self.spice_level =spice_level
#Explicit call method mai hum base class se initialize kar hai unsi properties ko but 
# yaha pe  properties ko init mai daal dete h ek saath aur jo nayi defined properties hoti hai issi class ke liye usse "self."  se varible mai declare karte hai

# The super() is a common method for inheriting the base class 
class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level
 #  yaha par super method use hai same explicit jaisa chai ki jagah "super()" use karte hai baaki nayi properties ko "self." se varible ai declare karte hai "