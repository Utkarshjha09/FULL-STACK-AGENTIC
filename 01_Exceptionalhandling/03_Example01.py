Friends_list = {"Ritik": 23, "Sushant": 23,"Utkarsh":25, "Satyam":21, "Niraj":20,"Vikash":24}

try:  # agar gum direcct search karte to yeh error dedeta as upar list mai yeh "Shivam" nhi hai toh error dega aur next line execute nhi hoga 
    Friends_list["Shivam"]    # toh agar maan lo agar koi real time live application mai aisa ho toh koi kuch search kare aur code mai error aa jaye isiliye hum "try"& "except" use karte haia 
except KeyError:  
    print("The Key that You are  trying to access does not exists")

print("Hello This is SHADOW aka.Utkarsh Jha")

# try usse "Statement" & "Query" ko try karta khojne ka 
# except  bolta hai ki agar koi error aya keyerror , typeerror , indexerror , aaya toh "something print kar de " nhi toh chaaahe toh next line pe execute ho jaye 

