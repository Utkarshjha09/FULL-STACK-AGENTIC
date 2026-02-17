# yaha par basically hum rew mai diye huye item ko array mai change karke print kar rhe hai jiske 
# liye humne ek funnction banya jisko static method ke andar jo ki array mai change karke print kar dega 
# static method mai hum function banate hai 
#   dusra tarika ye tha ki hum ek object banate 
# object = Chaiutils()
# obj.clean_ingredients(raw)

class ChaiUtils:
    @staticmethod 
    def clean_ingredients (text):
        return[item.strip() for item in text.split(",")]
    
raw = " water , milk ,  ginger , honey "
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)