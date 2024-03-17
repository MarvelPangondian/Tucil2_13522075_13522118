# Tugas kecil 2 Strategi Algoritma
> Program membuat Kurva Bézier dengan algoritma *Divide and Conquer* serta algoritma *Brute Force*

## Daftar Isi
- [Tugas kecil 2 Strategi Algoritma](#tugas-kecil-2-strategi-algoritma)
  - [Daftar Isi](#daftar-isi)
  - [Sistematika File](#sistematika-file)
  - [Deskripsi Program](#deskripsi-program)
  - [Requirements](#requirements)
  - [Menjalankan Program](#menjalankan-program)
  - [Status Proyek](#status-proyek)
  - [Identitas Pembuat Program](#identitas-pembuat-program)


<!-- * [License](#license) -->
## Sistematika File
```
├─── bin
│       ├─── 
│
├─── doc
│       ├─── Spesifikasi Tugas Kecil 2 Stima 2023_2024.pdf
│       └─── Tucil2_13522075_13522118.pdf
│
├─── src
│       ├─── bezier_curve
│       ├─── brute_force_bezier
│       ├─── dnc_bezier.py
│       ├─── IO.py
│       └─── main.py
│
├─── test
│       └─── All experiments and graph said experiments
│
├─── .gitignore
├─── README.md
└─── requirements.txt
```

## Deskripsi Program
Program untuk mencari Kurva Bézier menggunakan algoritma *Divide and Conquer* serta algoritma *Brute Force*. Program akan meminta orde serta titik kontrol Kurva Bézier dan iterasi yang diinginkan pengguna.

## Requirements
* Python version 3.12.2 or higher
* Pip version 24.0
* Matplotlib version 3.8.3
* Numpy version 5.15.10
* PyQt5 version 5.15.10
* PySide6 version 6.6.2

## Menjalankan Program
Pada *windows* atau *linux*, pastikan berada pada *root directory*. Pastikan dependencies sudah diinstall semua sesuai dengan requirements. Dependencies dapat diinstal dengan cara berikut
```
pip install requirements.txt
```
setelah semua selesai diinstal, pindah ke directory *src* dan jalankan main.py dengan cara berikut :
```
cd src
python main.py
```
jika command python tidak ada, kemungkinan command tersebut menggunakan nama lain seperti python3.
```
cd src
python3 main.py
```
Program ada kemungkinan kecil tidak berjalan di *linux* atau *macOS*. Sehingga sangat disarankan untuk menggunakan *windows*.</br>
berikut adalah tampilan utama 

```
=============================================================================
Bézier Curve Program
By : 
Marvel Pangondian (13522075)
Berto Richardo Togatorop (13522118)
=============================================================================
Choose your prefered algorithm !
1. Divide and Conquer
2. Brute Force
Input :
```
Pengguna akan diminta untuk memilih jenis algoritma yang ingin digunakan. setelah itu pengguna diminta mengisi orde, titik kontrol, serta iterasi. Berikut contoh tampilan program untuk kurva Bézier dengan orde 2, titik kontrol (1,2), (1,10), (5,10), serta iterasi 5.

```
=============================================================================
Choose your prefered algorithm !
1. Divide and Conquer
2. Brute Force
Input : 1

=============================================================================
Bézier Curve order :
Input is invalid !

Bézier Curve order : 2
X-axis Control point number  1: 1
Y-axis Control point number  1: 2
X-axis Control point number  2: 1
Y-axis Control point number  2: 10
X-axis Control point number  3: 5
Y-axis Control point number  3: 10
Input number of iterations: 5

```
Jika pengguna memilih menggunakan algoritma *Brute Force* (pilihan 2), maka graph akan langsung muncul di layar, tetapi jika pengguna memilih menggunakan algoritma *Divide and Conquer* (pilihan 1), pengguna dapat memilih dua macam tampilan, yakni graph saja atau graph dengan animasi.

```
=============================================================================
Please pick your prefered output
1. Graph, no animation
2. Graph with animation (bonus)
Input:  
```
Sangat disarankan untuk tidak memilih *Graph with animations* untuk kurva dengan iterasi lebih dari 6, sebab animasi akan sangat lama karena animasi menampilkan *step by step process*, dan untuk iterasi lebih dari 6 sudah sangat banyak *steps* nya.</br></br>

Setelah graph / animasi selesai ditampilkan, pengguna perlu *close* tampilan graph dengan memencet tombol X merah pada tampilan graph.</br></br>
berikutnya, pengguna memiliki opsi untuk menyimpan graph dalam bentuk .png, gambar akan disimpan di folder *test*, pastikan input nama tidak ada di folder *test* serta menyertakan ekstensi png.

```
=============================================================================
Would you like to save the graph ? y(yes) / other key (no): y
file name (with .png): bf1.png
File already exists !

Would you like to save the graph ? y(yes) / other key (no): y
file name (with .png): test.png 

Apakah ingin lanjut?(y/n) y
```
Pengguna dapat lanjut membuat atau menghentikan program.


## Status Proyek
Status : *Completed*
| Poin  | Ya | Tidak |
|---|---|---|
| Program berhasil dijalankan | ✓ |   |
| Program dapat melakukan visualisasi kurva Bézier | ✓ |   |
| Solusi yang diberikan program optimal | ✓ |   |
| Program dapat membuat kurva untuk n titik kontrol **(bonus)**|✓ |   |
| Program dapat melakukan visualisasi proses pembuatan kurva **(bonus)**|✓ |   |


## Identitas Pembuat Program
Nama : Marvel Pangondian </br>
NIM : 13522075 </br>
Profile Github : [MarvelPangondian](https://github.com/MarvelPangondian)

Nama : Berto Richardo Togatorop </br>
NIM : 13522118 </br>
Profile Github : [BertoRichardo](https://github.com/BertoRichardo)


