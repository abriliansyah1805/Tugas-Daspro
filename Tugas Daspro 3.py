def hitung_gaji(gaji_pokok, hari_kerja_per_minggu, jam_kerja_per_hari):
    gaji_harian = gaji_pokok / ((hari_kerja_per_minggu*4) * jam_kerja_per_hari)

    gaji_mingguan = (gaji_harian*jam_kerja_per_hari) * hari_kerja_per_minggu

    gaji_bulanan = gaji_mingguan * 4

    return gaji_harian, gaji_mingguan, gaji_bulanan

gaji_pokok = int(input("Masukkan gaji pokok: "))
hari_kerja_per_minggu = 6
jam_kerja_per_hari = 8

gaji_harian, gaji_mingguan, gaji_bulanan = hitung_gaji(gaji_pokok, hari_kerja_per_minggu, jam_kerja_per_hari)

print("Gaji Harian:" , gaji_harian, "/jam")
print("Gaji Mingguan:" , gaji_mingguan, "/minggu")
print("Gaji Bulanan:", gaji_bulanan, "/bulan")

print("1. Pilih Rincian Gaji Harian")
print("2. Pilih Rincian Gaji Mingguan")
print("3. Pilih Rincian Gaji Bulanan")
print("4. Selesaikan Program")

pilihan = int(input("Pilih Rincian Gaji [1/2/3/4] :"))
if pilihan == 1 :
    print("Rincian Gaji Harian")
    print("Gaji Harian:",  gaji_harian, "/jam")
elif pilihan == 2 :
    print("Rincian Gaji Mingguan")
    print("Gaji Mingguan:",  gaji_mingguan, "/minggu")
elif pilihan == 3 :
    print("Rincian Gaji Bulanan")
    print("Gaji Bulanan:",  gaji_bulanan, "/bulan")
else :
    print("program selesai")