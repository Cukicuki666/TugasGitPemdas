data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# no 1 :menampilkan seluruh data dari data panen
print("1.",data_panen)

#Menambahkan jarak antara nomor agar tidak meyatu outputnya
print()

#no 2 :menampilkan jumlah hasil panen jagung dari lokasi 2
print("2.Jumlah Hasil panen jagung dari Lokasi 2 Yaitu:", data_panen["lokasi1"]["hasil_panen"]["jagung"], "kg")

print()

#no3 :Menampilan nama lokasi dari lokasi3
print("3.Nama lokasi dari lokasi 3 Yaitu:", data_panen["lokasi3"]["nama_lokasi"])

print()

#no 4 :Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda.
total_padi = sum([data_panen[f'lokasi{i}']['hasil_panen']['padi'] for i in range(1, 6)])
total_kedelai = sum([data_panen[f'lokasi{i}']['hasil_panen']['kedelai'] for i in range(1, 6)])

print(f"4. Total hasil panen padi Semua Lokasi: {total_padi}")
print(f"4. Total hasil panen kedelai Semua Lokasi: {total_kedelai}")

print()

#no 5 : variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.
padi1, padi2, padi3, padi4, padi5 = (
    data_panen['lokasi1']['hasil_panen']['padi'],
    data_panen['lokasi2']['hasil_panen']['padi'],
    data_panen['lokasi3']['hasil_panen']['padi'],
    data_panen['lokasi4']['hasil_panen']['padi'],
    data_panen['lokasi5']['hasil_panen']['padi']
)

kedelai1, kedelai2, kedelai3, kedelai4, kedelai5 = (
    data_panen['lokasi1']['hasil_panen']['kedelai'],
    data_panen['lokasi2']['hasil_panen']['kedelai'],
    data_panen['lokasi3']['hasil_panen']['kedelai'],
    data_panen['lokasi4']['hasil_panen']['kedelai'],
    data_panen['lokasi5']['hasil_panen']['kedelai']
)

print("5.Jumlah hasil panen padi dari setiap lokasi:")
print(f"Lokasi 1: {padi1}, Lokasi 2: {padi2}, Lokasi 3: {padi3}, Lokasi 4: {padi4}, Lokasi 5: {padi5}")

print("\n5.Jumlah hasil panen kedelai dari setiap lokasi:")
print(f"Lokasi 1: {kedelai1}, Lokasi 2: {kedelai2}, Lokasi 3: {kedelai3}, Lokasi 4: {kedelai4}, Lokasi 5: {kedelai5}")

print()

#no 6:Percabangan untuk setiap lokasi
for lokasi in range(1, 6):
    padi = data_panen[f'lokasi{lokasi}']['hasil_panen']['padi']
    jagung = data_panen[f'lokasi{lokasi}']['hasil_panen']['jagung']
    
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {lokasi} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {lokasi} dalam kondisi baik.")

print()