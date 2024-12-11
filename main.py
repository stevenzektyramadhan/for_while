list_kota = ['jakarta','surabaya','depok','bekasi','solo','jogjakarta', 'semarang','makasar']



find_kota = input("ketik nama kota yang ingin kamu cari: ")

for i, kota in enumerate(list_kota):
    if kota.lower() == find_kota.lower():
        print(f'kota yang anda cari berada di indeks ke-{i}')
        break
    else:
        print('maaf , kota tidak ditemukan')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# for i in range(5):
#     print(f"perulangan ke-{i}")
    
    
for i in range(1,100,2):
    print(i)
    
tuple_buah = ('mangga','jeruk','apel','pepaya')

for buah in tuple_buah:
    print(buah)