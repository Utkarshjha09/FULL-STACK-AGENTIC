def calculate_bill(cups, PricePercup):
    tax_rate=0.18
    discount= {"GET10":0.1 , "GET20":0.20 , "GET30":0.30}.get("GET10",0)
    if (discount == 0):
        bill =cups*PricePercup + (cups*PricePercup*tax_rate)
    else:
        print(f"Enter Your Discount Code Applied:"{UserInput})
        bill = (cups*PricePercup - discount) + ((cups*PricePercup - discount)*tax_rate)

    return bill
Table1_bill =calculate_bill(15,10)
print(f"Bill of Table 1 is:{Table1_bill}")