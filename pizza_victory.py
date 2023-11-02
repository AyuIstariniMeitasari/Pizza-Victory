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
