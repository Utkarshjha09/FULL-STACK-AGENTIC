device_status = "Active"
Temperature=int(input("Enter the temperature of the Device :"))
if device_status == "Active":
    if (Temperature>38):
        print("Temperature is high")
    elif (Temperature<32):
        print("Temperature is Low")
    else :
        print("Temperature is Normal")
else:
    print("Your Device is offline ")