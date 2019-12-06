daftarnilai = {}
while True:
    print("===========================================================")
    print("==============Program Input Nilai Mahasiswa================")
    print("===========================================================")
    print("   Silahkan inputkan huruf depan dari menu yang tersedia   ")
    print("===========================================================")
    m = input("[ (T)ambah, (L)ihat, (U)bah, (H)apus, (Cari), (K)eluar ] : ")
    if m.lower() == 'k':
        break
    elif m.lower() == 't':
        print("Tambah Daftar Nilai Mahasiswa")
        nama =input("Masukan Nama Mahasiswa : ")
        nim = input("Masukan NIM            : ")
        tugas = int(input("Masukan Nilai Tugas    : "))
        uts = int(input("Masukan Nilai UTS      : "))
        uas = int(input("Masukan Nilai UAS      : "))
        akhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
        daftarnilai[nama] = nim, tugas, uts, uas, akhir
        print("")
    elif m.lower() == 'l':
        if daftarnilai.items():
            print("Lihat Daftar Nilai Mahasiswa")
            print("~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~")
            print("=================================================================")
            print("| No |       NAMA       |    NIM    | Tugas | UTS | UAS | Akhir |")
            print("=================================================================")
            i=0
            for x in daftarnilai.items():
                i+=1
                print("| {6:2d} | {0:16s} | {1:9s} | {2:5} | {3:3} | {4:3} | {5:2.2f} |"\
                  .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("=================================================================")
            print("")
        else:
            print("~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~")
            print("=================================================================")
            print("| No |       NAMA       |    NIM    | Tugas | UTS | UAS | Akhir |")
            print("=================================================================")
            print("|                  Tidak Ada Daftar Nilai                       |")
            print("=================================================================")
            print("")
    elif m.lower() == 'h':
        print("Hapus Daftar Nilai Mahasiswa")
        nama = input("Nama Mahasiswa : ")
        if nama in daftarnilai.keys():
            del daftarnilai[nama]
            print("")
        else:
            print("Mahasiswa {0} tidak ada".format(nama))
            print("")
    elif m.lower() == 'c':
        print("Cari Daftar Nilai Mahasiswa")
        nama = input("Nama Mahasiswa : ")
        if nama in daftarnilai.keys():
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
           print("====================================================================================================")
           print("Daftar Nilai {0} adalah ('Nim',Tugas,UTS,UAS,Akhir) => {1}"\
                 .format(nama, daftarnilai[nama]))
           print("====================================================================================================")
           print("")
        else:
            print("~~~~~~~~~~~~~~~~~~~~Daftar Nilai Mahasiswa~~~~~~~~~~~~~~~~~~~~~~~")
            print("=================================================================")
            print("               Daftar Nilai {0} tidak ada                      "\
                  .format(nama))
            print("=================================================================")
            print("")
    elif m.lower() == 'u':
        print("Ubah Daftar Nilai Mahasiswa")
        nama = input("Nama Mahasiswa   : ")
        if nama in daftarnilai.keys():
            nim = input("NIM Baru         : ")
            tugas = int(input("Nilai Tugas Baru : "))
            uts = int(input("Nilai UTS Baru   : "))
            uas = int(input("Nilai UAS Baru   : "))
            akhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
            daftarnilai[nama] = nim, tugas, uts, uas, akhir
            print("")
        else:
            print("=================================================================")
            print("Daftar Nilai {0} tidak ada".format(nama))
            print("=================================================================")
            print("")
    else:
        print("Pilih menu yang tersedia")
        print("")
