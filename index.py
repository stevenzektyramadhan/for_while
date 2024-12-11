list_kota = ["jakarta","bandung","surabaya","pekalongan","bekasi","pangkal pinang","mentok"]

find_kota = input("masukan nama kota: ")
i = 0
while i < len(list_kota):
    if list_kota[i].lower() == find_kota.lower():
        print(list_kota[i])
        break
    print("bukan",list_kota[i])
    i +=1
else:
        print('maaf , kota tidak ditemukan')



