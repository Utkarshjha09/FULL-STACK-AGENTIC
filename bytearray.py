raw_spice_data=bytearray(b'CINNAMON')
raw_spice_data.replace(b'CINNA', b'CARD') # here in this line i will not print the updated value it will store the value inside the raw_spice_data variable
raw_spice_data= raw_spice_data.replace(b'CINNA', b'CARD') # in this variable is updated with the updated value 
print(f"Bytes -:{raw_spice_data}")