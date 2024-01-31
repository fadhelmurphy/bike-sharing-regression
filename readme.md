# Product Requirement / Business Problem Understanding

## Background

Capital Bike Share adalah perusahaan penyedia layanan sewa sepeda yang telah menjadi pilihan utama penduduk dan pengunjung di wilayah ibu kota, beroperasi di Washington D.C., Amerika Serikat. Beroperasi selama lebih dari lima tahun, Capital Bike Share telah menyebar ribuan sepeda di berbagai lokasi strategis di sekitar kota, menyediakan solusi transportasi yang nyaman dan berkelanjutan bagi pelanggan mereka. Dengan komitmen terhadap teknologi canggih dan layanan yang ramah pengguna, Capital Bike Share terus berupaya meningkatkan pengalaman peminjaman sepeda bagi semua orang. Sepeda-sepeda tersebut tersedia di stasiun-stasiun yang tersebar di seluruh kota, termasuk di sekitar area pusat kota, taman-taman, dan tempat-tempat umum lainnya yang ramai.

Industri penyewaan sepeda berkembang pesat, terutama dengan adanya layanan berbagi sepeda di berbagai kota. Perusahaan penyedia layanan ini memiliki keinginan untuk meningkatkan efisiensi operasionalnya melalui prediksi permintaan sepeda pada kondisi tertentu. Data yang dimiliki oleh perusahaan tersebut terdapat dalam dataset data_bike_sharing.csv, yang mencakup informasi seperti waktu, cuaca, dan jumlah sepeda yang dipinjam.

## Context

Capital Bike Share, penyedia layanan sewa sepeda terkemuka di Washington D.C., Amerika Serikat, berkomitmen untuk meningkatkan efisiensi operasional dan pengalaman pengguna mereka. Dalam upaya mencapai tujuan ini, perusahaan telah mengumpulkan dataset harian yang mencakup informasi beragam, termasuk kelembapan, kondisi cuaca, hari libur, musim, suhu yang dirasakan, jam dalam sehari, dan hari dalam seminggu. **Membangun model prediksi jumlah total peminjaman sepeda berdasarkan faktor-faktor seperti kelembapan, kondisi cuaca, hari libur, musim, suhu yang dirasakan, jam dalam sehari, dan hari dalam seminggu menjadi krusial untuk mendukung tujuan Capital Bike Share dalam meningkatkan layanan dan efisiensi operasional**. Dengan pemahaman yang lebih baik tentang tren penggunaan sepeda berdasarkan variabel-variabel tersebut, perusahaan dapat **mengoptimalkan stok sepeda di setiap stasiun, mengatur penempatan sepeda sesuai permintaan, dan meningkatkan ketersediaan sepeda untuk memenuhi kebutuhan pengguna**. Dengan demikian, model prediksi ini akan membantu Capital Bike Share untuk meningkatkan pengalaman pengguna, mengoptimalkan operasi, dan memperkuat posisinya di pasar layanan sewa sepeda di Washington D.C.

## Problem Statement
Tujuan utama proyek ini adalah **memprediksi jumlah total peminjaman sepeda setiap hari berdasarkan faktor-faktor seperti kondisi cuaca, musim, suhu, dan lainnya**. Dengan pemahaman yang lebih baik tentang tren penggunaan sepeda, penyelenggara layanan dapat mengoptimalkan stok sepeda, mengelola penempatan sepeda di berbagai lokasi, dan meningkatkan ketersediaan sepeda sesuai dengan permintaan.

## Goals

  - Membangun model prediksi jumlah total peminjaman sepeda setiap hari berdasarkan variabel-variabel seperti kelembapan, kondisi cuaca, hari libur, musim, suhu yang dirasakan, jam dalam sehari, dan hari dalam seminggu.

## Analytic Approach

Pendekatan analitis yang akan digunakan melibatkan pemodelan regresi, di mana model machine learning akan dibangun untuk memahami hubungan antara variabel-variabel seperti kelembapan, kondisi cuaca, musim, dan lainnya dengan jumlah total peminjaman sepeda. 

**Pemilihan Variabel**: Memilih variabel yang signifikan untuk membangun model prediksi jumlah total sepeda.

**Pemisahan Dataset**: Membagi dataset menjadi set pelatihan dan set pengujian.

**Pembangunan Model Regresi**: Menggunakan algoritma regresi untuk memprediksi jumlah total sepeda.

**Penyetelan Model**: Penyesuaian hiperparameter untuk meningkatkan kinerja model.

**Evaluasi Kinerja**: Menggunakan metrik seperti RMSE, MAE, MAPE untuk menilai skor prediksi.

## Metric Evaluation

- **RMSE (Root Mean Squared Error)**:

  - **Tujuan**: Meminimalkan kesalahan total, dengan penekanan pada kesalahan yang lebih besar.
  - **Alasan**: RMSE memberikan penalti lebih besar untuk kesalahan yang lebih besar, yang dapat bermanfaat jika bisnis memiliki toleransi yang lebih rendah terhadap kesalahan yang signifikan. Dalam skenario peminjaman sepeda, jika kesalahan prediksi yang signifikan dapat menyebabkan masalah operasional atau keuangan, RMSE dapat memberikan pandangan yang lebih baik tentang tingkat kesalahan yang dapat diharapkan secara keseluruhan.
  - **Contoh**: Jika RMSE adalah 3, itu berarti model mengalami kesalahan sekitar 3 peminjaman sepeda secara keseluruhan. Jika bisnis memiliki sensitivitas terhadap kesalahan yang signifikan, fokus pada RMSE dapat membantu mengidentifikasi dan memitigasi prediksi yang secara signifikan keliru.

- **MAPE (Mean Absolute Percentage Error)**:

  - **Tujuan**: Meminimalkan kesalahan relatif dalam persentase antara prediksi dan nilai sebenarnya.
  - **Alasan**: MAPE memberikan perspektif kesalahan relatif, yang dapat membantu memahami sejauh mana prediksi dapat diandalkan dalam skala persentase. Dalam konteks bisnis peminjaman sepeda, jika persentase kesalahan memiliki dampak yang signifikan pada keputusan operasional atau kebijakan, MAPE dapat memberikan informasi yang lebih relevan tentang kualitas prediksi.
  - **Contoh**: Jika MAPE adalah 10%, itu berarti rata-rata kesalahan relatif adalah 10%. Jika bisnis memiliki batasan toleransi persentase kesalahan, maka MAPE yang lebih rendah akan menunjukkan tingkat akurasi yang lebih tinggi sesuai dengan tujuan tersebut.

- **Mean Absolute Error (MAE)**:

  - **Tujuan**: Meminimalkan kesalahan absolut rata-rata antara prediksi dan nilai sebenarnya.
  - **Alasan**: MAE memberikan gambaran langsung tentang seberapa dekat prediksi dengan data aktual tanpa memperhitungkan arah kesalahan. Dalam konteks peminjaman sepeda, bisnis mungkin lebih peduli dengan seberapa akurat prediksi jumlah sepeda yang sebenarnya dipinjam, tanpa memandang apakah prediksi lebih tinggi atau lebih rendah dari nilai sebenarnya. MAE sangat sesuai untuk mengukur tingkat kesalahan ini secara absolut.
  - **Contoh**: Jika MAE adalah 2, itu berarti model secara rata-rata mengalami kesalahan sekitar 2 peminjaman sepeda per hari. Jika bisnis menetapkan batasan toleransi kesalahan harian, maka MAE yang lebih rendah akan menunjukkan model yang lebih sesuai dengan tujuan ini.


## Stakeholders

**Penyelenggara Layanan Sewa Sepeda**: Menggunakan hasil prediksi untuk mengoptimalkan stok sepeda, meningkatkan efisiensi operasional, dan memahami pola permintaan pengguna.
**Pengguna Sepeda**: Mendapatkan manfaat dari ketersediaan sepeda yang lebih baik dan pelayanan yang dioptimalkan berdasarkan pola penggunaan sepeda.

## Release

[Model Release (Higher is better)](https://github.com/fadhelmurphy/bike-sharing-regression/releases)

# Project Architecture

Project ini dilengkapi CI/CD yang mana dapat upload model jika push ke tag. contoh:

`git tag v0.0.11-xgbregressor`

`git push origin v0.0.11-xgbregressor`

maka akan otomatis upload model dengan versioning. Dengan adanya versioning ini memudahkan Software Engineer dalam melakukan rollback ke versi sebelumnya jika di versi terbaru masih terdapat bug.