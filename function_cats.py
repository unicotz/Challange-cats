def checkCats(CatsTuti, CatsNining):
    # Salin array milik Tuti
    correctedCatsTuti = CatsTuti.copy()

    # Hapus usia kucing dari kucing pertama dan dua kucing terakhir
    correctedCatsTuti[0] = "Anjing"  # Kucing pertama adalah anjing
    correctedCatsTuti[-1] = "Anjing"  # Kucing terakhir adalah anjing
    correctedCatsTuti[-2] = "Anjing"  # Kucing kedua dari belakang adalah anjing

 

    # Gabungkan data Tuti yang sudah dikoreksi dengan data Nining
    combinedCats = correctedCatsTuti + CatsNining

    # Inisialisasi array untuk menyimpan status setiap hewan
    statusHewan = []

    # Loop melalui setiap hewan dan tampilkan apakah itu kucing dewasa atau kucing kecil
    for i, hewan in enumerate(combinedCats):
        if isinstance(hewan, int):
            if hewan < 3:
                statusHewan.append(f"Pemilik Kucing Nomor {i+1} masih anak-anak ({hewan} tahun)")
            else:
                statusHewan.append(f"Pemilik Kucing Nomor {i+1} adalah kucing dewasa dan berusia {hewan} tahun")
        else:
            statusHewan.append(f"Pemilik Hewan Nomor {i+1} yang ditanya Tuti memiliki {hewan}, bukan kucing")

    # Membuat array yang berisi data Tuti yang sudah dikoreksi dan data Nining
    combinedData = correctedCatsTuti + CatsNining

    # Menampilkan status setiap hewan di konsol
    for status in statusHewan:
        print(status)

    return combinedData

# Contoh penggunaan fungsi
CatsTuti = [3, 5, 2, 12, 7]
CatsNining = [4, 1, 8, 3, 13]

combinedData = checkCats(CatsTuti, CatsNining)
