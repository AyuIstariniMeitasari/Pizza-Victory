print("------Welcome to our Pizza Victory------")

#Silahkan dipilih menunya 
print("\nMenu Pizza:")
print("1. Pizza Frankfurter BBQ Rp 43,637 ")
print("2. Pizza Meat Monsta Rp 43,637 ")
print("3. Pizza Super Supreme Rp 43,637 ")
print("4. Pizza Super Supreme Chicken Rp 43,637 ")

#input pesanan pizza
pesan_pizza = int(input("Pilih jenis pizza [1/2/3/4]:"))

#pesan pizza
if pesan_pizza == 1 :
    harga_pizza = 43637
elif pesan_pizza == 2 :
    harga_pizza = 43637
elif pesan_pizza == 3 :
    harga_pizza = 43637
elif pesan_pizza == 4:  
    harga_pizza = 43637
else:
    print("Pilihan menu pizza tidak valid.")
    exit()
#Silahkan dipilih crust pizza  
print("\nMenu Crust Pizza:")              
print("1. Pan Rp 0 ")
print("2. Cheesy bite Rp 10,000 ")
print("3. Stuffed Rp 15,000 ")
print("4. Crown Rp 18,000 ")

#input tambahan crust
crust_pizza = int(input("Pilih crust pizza [1/2/3/4]:"))

#pesan crust
if crust_pizza == 1 : 
    harga_crust = 0
elif crust_pizza == 2 : 
    harga_crust =  10000
elif crust_pizza == 3 : 
    harga_crust = 15000
elif crust_pizza == 4 :
    harga_crust = 18000   
else:
    print("Pilihan crust tidak valid.")    
    exit()

#Silahkan dipilih size pizza                 
print("1. Personal Rp 0")
print("2. Reguler Rp 15,000")
print("3. Large Rp 20,000")
print("4. Extra large Rp 25,000")
print("5. Double extra large Rp 30,000")
print("6. Super extra large Rp 35,000")

#input tambahan size
size_pizza = int(input("Pilih size [1/2/3/4/5/6]: "))

#pesan size
if size_pizza == 1 : 
    harga_size = 0
elif size_pizza == 2 : 
    harga_size =  15000
elif size_pizza == 3 : 
    harga_size = 20000
elif size_pizza == 4 :
    harga_size = 25000
elif size_pizza == 5 :
    harga_size = 30000
elif size_pizza == 6 :
    harga_size = 35000   
else:
    print("Pilihan size tidak valid.")    
    exit()

#Tambahan varian cheese
print ("Ekstra keju atau tidak (fee  :  Rp.  13.000)")
print ("1. Ya")
print ("2. Tidak")
ekstra_keju = input("Pilih ekstra keju ]1/2]: ")
if ekstra_keju == "1" :
    harga_keju = 13000
elif ekstra_keju == "2" :
    harga_keju = 0
else:
    print("Pilihan ekstra keju tidak valid.")    
    exit()

total_harga =  harga_pizza + harga_size + harga_size + harga_keju 
print("Terimakasih telah membeli pizza di Victory Pizza")
print("Total pesanan anda : Rp. ", int(total_harga))
