#Nama  : Muhammad Risky Alpianur
#NIM   : 2509116101
#Kelas : C

users = {"Kiwah":{"password":"101","role":"manager"},
         "Orang":{"password":"098","role":"karywan"}}

portofolio = {"BTC":{"jumlah":"20","harga":"200000000"},
              "ERH":{"jumlah":"5","harga":"3000000"},
              "XRP":{"jumlah":"70","harga":"71000000"}
              }
        
def Masukan():
    try:
        nama = input("Masukkan nama saham/cryto : ")
        jumlah = float(input("Masukkan jumlah saham/cryto : "))
        harga = float(input("Masukkan harga beli : "))
        portofolio [nama] =  {"jumlah": jumlah, "harga": harga}
        print("Aset berhasil ditambahkan!")
    except ValueError:
        print("wajib di isi angka contohnya = (1")
        return "silahkan pilih dan isi ulang kembali"
def ubah():
    try:
        nama = input("nama aset yang ingin diubah : ")
        if nama in portofolio:
            harga = float(input("Ubah harga : "))
            portofolio[nama]["harga"] = harga
            print(f"Aset '{nama}' berhasil diubah menjadi Rp. {harga}.")
        else:
            print(f"Aset '{nama}' tidak ditemukan.")
    except ValueError:
        print("wajib di isi angka contohnya = (1")
        return "silahkan pilih dan isi ulang kembali"

def lihat():
        for nama, aset in portofolio.items():
            jumlah = aset["jumlah"]
            harga = aset["harga"]
            print(f"Nama Aset : {nama}")
            print(f"Jumlah    : {jumlah}")
            print(f"Harga     : Rp. {harga}")
            print("-" * 30)
        if len(portofolio) == 0:
         return "Silahkan tambahkan aset"
def hapus():
    nama= input("Menu yang ingin dihapus : ")
    if nama in portofolio:
            del portofolio[nama]
            print(f"Aset '{nama}' berhasil dihapus.")
    else:
            print(f"Aset '{nama}' tidak ditemukan.")

for percobaan in range(1,2):
    print("-"*32)
    username = input("masukan username :")
    password = input("masukan password :")
    role = input("masukan Jabatan :")

    if username in users and users[username]["password"] == password and users [username]["role"] == role:
        print(f"Login berhasil sebagai {users[username]['role']}")
        print("selamat datang")
    else:
        sisa_coba = 2 - percobaan
        if sisa_coba > 0:
            print(f"username atau password atau jabatan yang anda masukan salah.")
            exit()
        else:
            print("sisa login anda habis")
            exit()
while True:
    print("\n","="*17,"Daftar Menu","="*17)
    print("1. Melihat Aset")
    print("2. Menambahkan Aset")
    print("3. Mengubah Aset")
    print("4. Menghapus Aset")
    print("5. Keluar")


    inpus = input("Pilih salah 1-5 :")

    if inpus == "1":
        print(lihat())
    elif inpus == "2":
        print(Masukan())
    elif inpus == "3":
        print(ubah())
    elif inpus == "4":
        print(hapus())
    elif inpus == "5":
        print("program telah berhenti")
        break

    else:
        print("pilihan harus 1-5 tidak terima huruf.")
