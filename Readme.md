# Analisa Sentimen Review Kategori Elektronik Di Amazon

# Rivai Hayashi Hendrik Talenggoran

## 1. Pendahuluan
- **Tujuan:** Menggali dan menganalisa informasi terkait sentimental review pengguna Amazon di kategori elektronik
- **Latar Belakang:Kebutuhan elektronik di zaman sekarang sudah menjadi hal yang umum, mengigat perkembangan teknologi yang
                    Semakin berkembang dan kemajuan zaman yang semakin pesat berkat adanya bantuan dari teknologi. Projek ini dibuat
                    untuk menganalisa review sentimen  di kategori elektronik Amazon untuk melihat bagaimana tanggapan dan respon pengguna
                    terhadap barang elektronik yang dijual di amazon. Projek ini bertujuan agar kita  bisa lebih melihat kualitas penjualan dan
                    dan barang elektronik yang ada di amazon lewat analisa sentimen review yang ada.** 

## 2. Sumber Data
- **Deskripsi Sumber Data:**
  - **https://amazon-reviews-2023.github.io/**
  

- **Struktur Data:**
  - **Tipe data:**  `String`, `Float`, `List`,`Dictionary`,`Series`,`TimeStamp`
  - **Data yang dikumpulkan:** `rating`, `title`, `text`, `images`, `asin`,`parent_asin`,`user_id`,`timestamp`,`helpful_vote`,`verified_purchase`.
  

- **Metode Pengumpulan Data:** 
   - **Data diambil melalui situs https://amazon-reviews-2023.github.io/**
   - **Data yang dikumpulkan berjenis Data** `Kualitatif` dan `Kuantitatif`
   - **Kualitatif mencakup** `title`,`text`,`images`,`asin`,`parent_asin`,`user_id`,`verified_purchase`
   - **Kuantitatif mencakup** `rating`, `time_stamp`, `helpful_vote`
  
## 3. Pra-Processing Data
- **Proses Pembersihan Data:**
  - **Fitur Proses Pembersihan Data terdapat pada file** `PraProcessing.py`
  - **Hapus tag HTML** : Baris dengan nilai kosong dihapus


- **Pra-Pemrosesan Data:**
  - **Fitur Pra-Pemrosesan Data terdapat pada file** `PraProcessing.py`
  - **Lowecase                      :** Data dinormalisasikan agar seragam
  - **Hapus angka di title dan text :** Hapus angka karna tidak diperlukan untuk pemodelan
  - **Hapus karakter tidak penting  :** Hapus karakter yang tidak diperlukan
  - **Tokenisasi                    :** Untuk `title`,`text`, memisahkan kata
  - **Lematisasi                    :** Untuk `title`,`text`, menormalisasikan kata
  - **Ekstrak Tahun-Bulan-Tanggal   :** Untuk `time_stamp`


  
## 4. Eksplorasi Data
- **Fitur Eksplorasi Data terdapat pada file `EksplorasiData.py`**



## 5. Analisis dan Pemodelan Data
- **Fitur Eksplorasi Data terdapat pada file `AnalisisDanPemodelanData.py`**


## 6. Kesimpulan dan Rekomendasi
**Dari hasil eksplorasi dan analisis data, berikut merupakan hasil kesimpulan dan rekomendasi sementara:**

- **Kesimpulan**
  - **Distribusi Rating                 :** Dari hasil pengolaan data, menunjukkan bahwa rating terdistribusi lebih
                                             mengarah kepada rating tinggi(4-5), ini menunjukkan kepuasan konsumen terhadap 
                                             pembelian elektronik yang ada di Amazon
  - **Rata-Rata Rating berdasarkan Wakti :** Hasil analisa menunjukkan adanya peningkatan rating dari tahun ke tahun, menunjukkan bahwa
                                             baik produk kategori elektronik maupun mekanisme pembelian selalu dikembangkan untuk memudahkan 
                                             pengguna dalam mencari dan membeli produk elektronil
  - **Teks Yang sering muncul             :** Hasil visualisasi menunjukkan bahwa teks yang sering muncul kearah 'great, good, five star,love', menunjukkan
                                              bahwa sentimen komentar dari pengguna mengarah ke sentimen positif yang berarti pengguna puas terhadap baik produk maupun
                                              kualitasnya.

  - **Distribusi Gambar Per-Ulasan             :** Hasil visualisasi menunjukkan distribusi gambar pada penjualan berada di antara angka 1 dan 0 di hampir seribu penjualan
                                              ,menunjukkan bahwa pengguna cenderung tidak memakai gambar dalam review

  - **Distribusi Jumlah Vote Berguna per Ulasan:** Visualisasi yang ditampilkan menunjukkan bahwa distribusi vote berada pada rentang 0-50 dengan jumlah ulasan antara 0-120an
                                                    , menunjukkan jumlah vote berguna yang ada hanya sedikit
- **Rekomendasi**
  - **Peningkatan kualitas pelayanan     :** Hasil menunjukkan bahwa pengguna puas terhadat penjualan elektronik amazon, maka dari itu harus ditingkatan kualitas pelayanan yang ada di amazon agar pengguna tetap merasa nyaman dalam pelakukan pembelian produk eletronik di amazon



## 7. Penutup
Hasil analisa yang telah dilakukan penting agar kita bisa melihat perilaku konsumen terhadap penjualan yang ada di amazon
sehingga kita bisa memutuskan untuk melakukan pembelian atau tidak di amazon