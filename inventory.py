ulang = "ya"
while ulang == "ya":
    
    pilih = input("input data inventory baru(ya/tidak)?ya :")
    if pilih == "ya":
        inventory = input("Nama perangkat :")
        file = open("db-inventory.txt",'a')
        file.write("\n"+"Nama Perangkat :"+inventory)
        inventory = input("Lokasi :")
        file = open("db-inventory.txt",'a')
        file.write("\n"+"Lokasi :"+inventory)
    else:
        file = open("db-inventory.txt","r")
        print(file.read())
        break;

