#Soal 3

print("Program Python Deteksi bilangan prima atau bukan prima")
print("------------------------------------------------------")


for angka in range(10,25):
    if (angka==2 or angka==3 or angka==5 or angka==7) or (angka%2 != 0 and angka%3 !=0 and
    angka%5 != 0 and angka%7 !=0):
        print('{} adalah bilangan prima'.format(angka))
    else:
        print('{} bukan prima'.format(angka))

