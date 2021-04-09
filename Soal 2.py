#Soal 2

print("Program Python Hitung Rata Rata")
print("-------------------------------")

list_data = int(input("\nBerapa banyaknya data yang akan dihitung: "))
print()

angka = []
total = 0

for nilai in range(0, list_data):
    data_ke = int(input("Masukkan data yang ke-%d: " % (nilai+1)))
    angka.append(data_ke)
    total += angka[nilai]
    rata_rata = total / list_data

print("Jumlah nilai data adalah: %d " % total)
print("\nNilai rata ratanya adalah: {%0.1f} " % rata_rata)

