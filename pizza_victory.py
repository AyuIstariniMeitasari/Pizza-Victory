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
