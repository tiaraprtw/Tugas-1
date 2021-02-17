#sistem nilai siswa
Nama= str(input("Nama Siswa:"))
UT= float(input("Masukan Nilai Ujian Teori:"))
UP= float(input("Masukan Nilai Ujian Praktek:"))
if UT >= 70 and UP >= 70:
    print("Selamat, {} lulus!".format(nama))
elif UT >= 70 and UP < 70:
    print("Anda harus mengulang ujian praktek.")
elif UT < 70 and UP >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")
