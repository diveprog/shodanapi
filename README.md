![image](https://user-images.githubusercontent.com/95019755/149070447-092f7066-bd2a-40e7-a29f-327ef2f9f375.png)

----------------------------------------------------------------------------------------

# Bismillahirrahmanirrahim.

shodanapi.py merupakan program yang dibuat untuk melakukan scanning subdomain agar mempermudah 
proses recon pada metode Penetration Testing. Program ini menggunakan fitur search engine yang 
dimiliki shodan.io memanfaatkan Publik API dan Secret Key (dengan cara mendaftar akun).

----------------------------------------------------------------------------------------

# KEBUTUHAN

Untuk bisa menjalankan program ini diperlukan bahasa pemrograman Python dan instalasi dependensi / 
install library yang digunakan oleh Python agar dapat berjalan sebagaimana mestinya. Program ini 
berjalan pada CLI sehingga dibutuhkan 'command prompt' pada Windows atau 'Terminal' pada Linux / Nix 
Berikut cara melakukan instalasinya

- Unzip aplikasi menggunakan
 **Linux**

- sudo unzip sectrails.zip

**Windows**

- klik kanan pada folder > extract to folder

**Cek versi python dan pip dengan menjalankan command pada terminal**

- python3 --version
- pip3 --version

# _-Apabila belum memiliki Python dan pip-_
**Linux Debian**

- sudo apt install python3
- sudo apt install python3-pip / sudo install apt python-pip
- sudo apt update

**Windows**

- Kunjungi website https://www.python.org/downloads/
- Download Python versi 3 yang tertera pada awal halaman, berwarna kotak kuning
- Lakukan instalasi sebagaimana biasa pada Windows
- Apabila sudah selesai instalasi, buka command prompt dan arahkan ke folder dimana file tersimpan

**Cek versi python dan pip dengan menjalankan command pada command prompt**

- python3 --version
- pip3 --version

**Mac OS**

- brew install python3
- brew install python3-pip / sudo apt install  python-pip

----------------------------------------------------------------------------------------

# _-Apabila sudah terinstall Python maka langkah selanjutnya yakni instalasi library dengan command:_

- pip install -r requirements.txt
- pip3 install -r requirements.txt

Tunggu hingga proses selesai maka program siap untuk digunakan

----------------------------------------------------------------------------------------

# CARA PENGGUNAAN

agar dapat berjalan sebagaimana fungsinya diperlukan akses sebagai user tertinggi dalam hal ini 
root

- sudo python3 shodanapi.py

**--CONTOH PENGGUNAAN--**

![image](https://user-images.githubusercontent.com/95019755/149068147-e79cee7a-f738-4bf4-aa06-038cf7634c48.png)

masukkan nama domain tanpa menggunakan 'http' atau 'https' cth: domain.com

----------------------------------------------------------------------------------------

**-CATATAN-**

Hasil scan dalam format json akan langsung di simpan secara default dengan nama:
data_shodanapi.json

Kekurangan : 
-fitur search engine pada shodan hanya dapat diimplementasikan untuk mencari domain saja tidak 
dengan search engine tambahan yang dimiliki shodan seperti (hostname:"domain.com" / ssl:target.* 200 
/ ssl.cert.subject.CN:"domain.*" 200) karena dibutuhkan membership
-belum bisa membuat format JSON secara khusus

----------------------------------------------------------------------------------------

**Mohon maaf apabila ada fungsi yang tidak bejalan.**
