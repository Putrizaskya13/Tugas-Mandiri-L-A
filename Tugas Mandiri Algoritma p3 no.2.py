#Menentukan nilai terbesar diantara keempat bilangan.

b1 = 20
b2 = 60
b3 = 40
b4 = 100

if (b1 > b2) and (b1 > b3) and (b1 > b4):
    print(b1, "Adalah bilangan terbesar")
elif (b2 > b1) and (b2 > b3) and (b2 > b4):
    print(b2, "Adalah bilangan terbesar")
elif (b3 > b1) and (b3 > b2) and (b3 > b4):
    print(b3, "Adalah bilangan terbesar")
else:
    print(b4, "Adalah bilangan terbesar dari 4 bilangan yang diinputkan")
