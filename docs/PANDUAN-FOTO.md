# Panduan foto asli

Lo tinggal drag and drop foto ke folder yang sesuai, kemudian commit dan push. GitHub Actions otomatis membaca file foto. Untuk preview lokal, jalankan `python3 scripts/preview.py`, lalu refresh setelah perubahan terdeteksi.

## Format dan urutan

- JPG, JPEG, PNG, WEBP, AVIF, atau GIF. HEIC dari ponsel perlu diekspor ke JPG/WEBP terlebih dahulu.
- Gunakan `00-cover.jpg`, `01-proses.jpg`, `02-hasil.jpg` agar urutan jelas. Angka diurutkan secara natural, jadi 2 mendahului 10.
- Foto pertama menjadi cover. Foto berikutnya masuk galeri detail. Artikel hanya menggunakan foto pertama sebagai preview.
- Foto profil menggunakan file pertama; hero-design mendukung beberapa gambar desain asli.
- Folder kosong tidak membuat kotak kosong. Hapus foto lalu push untuk menghapusnya dari website.
- Nama file boleh mengandung spasi, tetapi nama sederhana lebih mudah dirawat.
- Rekomendasi ukuran 1200–2000 px dan sekitar 200–600 KB per foto agar halaman ringan. Kompres sendiri sesuai kebutuhan; build tidak mengubah foto asli.
- Foto tidak dibaca dari subfolder tambahan. Taruh langsung pada folder entri.

## Foto pembuka dan pendidikan

| Keperluan | Folder |
| --- | --- |
| Foto profil lo | `assets/photos/profile/` |
| Desain asli lo | `assets/photos/hero-design/` |
| Pendidikan UNAIR | `assets/photos/education/universitas-airlangga/` |

## Proyek

| Entri | Folder |
| --- | --- |
| ROV PEMALOE - Underwater 2D Mapping and Position Estimation ROV | `assets/photos/projects/rov-pemaloe/` |
| Stock Price Forecasting in Emerging Markets: A Controlled Empirical Evaluation with Consistent Feature Representation | `assets/photos/projects/stock-price-forecasting/` |
| PURE-it: Portable Utility for Rehabilitation & Examination Innovative Technology | `assets/photos/projects/pure-it/` |
| CKIA - Compact Kit for Introduction to Aquarobotics | `assets/photos/projects/ckia/` |
| Automatic VTuber Livestream Clipping Using Machine Learning - Case Study: Kaela Kovalskia | `assets/photos/projects/automatic-vtuber-clipping/` |
| MARVIC 2.5 - Autonomous Underwater Vehicle for SAUVC 2025 | `assets/photos/projects/marvic-2-5/` |
| Mini AGV Robot | `assets/photos/projects/mini-agv/` |
| Motorcycle Tubeless Tire Condition Monitoring Using Computer Vision | `assets/photos/projects/tire-condition-monitoring/` |
| MOBIV: Portable CD4 Monitoring System for HIV Patients Based on Microfluidic Optical Biosensor Integrated with Internet of Things (IoT) | `assets/photos/projects/mobiv/` |
| MARVIC 2.0 - Autonomous Underwater Vehicle for KRBAI 2024 | `assets/photos/projects/marvic-2-0/` |
| IoT Si-Tera (Sistem Tsunami Terintegrasi) | `assets/photos/projects/iot-si-tera/` |
| LINE FOLLOWER ROBOT | `assets/photos/projects/line-follower/` |
| MARVIC 1.0 - ROV Prototype | `assets/photos/projects/marvic-1-0/` |

## Pengalaman kerja

| Entri | Folder |
| --- | --- |
| Robotics & ROV Instructor | `assets/photos/work/sekolah-robot-indonesia/` |
| Freelance Robotics Instructor | `assets/photos/work/freelance-robotics-instructor/` |

## Internship

| Entri | Folder |
| --- | --- |
| Underwater Robotics Engineer Intern | `assets/photos/internship/surovotic/` |

## Organisasi

| Entri | Folder |
| --- | --- |
| Senior Support | `assets/photos/organization/mare-victor-senior-support/` |
| Human Resource Development Staff | `assets/photos/organization/kombo-human-resource-development/` |
| Team Leader | `assets/photos/organization/mare-victor-team-leader/` |
| Person in Charge | `assets/photos/organization/airofest/` |
| Vice Project Officer | `assets/photos/organization/rotation-2023/` |
| Head of the Science, Research and Technology Department | `assets/photos/organization/himatera-science-research-technology/` |
| External Relations Staff | `assets/photos/organization/kombo-external-relations/` |
| PKM Divison Staff | `assets/photos/organization/garuda-sakti-pkm/` |

## Penghargaan

| Entri | Folder |
| --- | --- |
| Gold Medalist - World Invention Competition and Exhibition (WICE) | `assets/photos/awards/wice-2025-gold/` |
| Finalist - Singapore AUV Challenge (SAUVC) 2025 | `assets/photos/awards/sauvc-2025-finalist/` |
| Bronze Medalist - PIMNAS 37, PKM-KC 2 Presentation Category | `assets/photos/awards/pimnas-37-bronze/` |
| Finalist - Kontes Robot Bawah Air Indonesia (KRBAI) | `assets/photos/awards/krbai-2024-finalist/` |
| Awardee - PKM-KC Pendanaan 2024 | `assets/photos/awards/pkm-kc-2024-funding/` |

## Articles & Features

| Entri | Folder |
| --- | --- |
| Gagas Monitor HIV Berbasis IoT, Tim MOBIV UNAIR Sabet Perunggu PIMNAS | `assets/photos/articles/mobiv-pimnas/` |
| PURE-it Karya Mahasiswa UNAIR Bawa Pulang Emas dari Ajang WICE 2025 di Malaysia | `assets/photos/articles/pure-it-wice/` |
| Perjalanan Tim MARVIC dalam KRBAI Tingkat Nasional | `assets/photos/articles/marvic-krbai/` |
| Cetak Jejak di Singapura, MARE VICTOR Bertanding di SAUV Challenge 2025 | `assets/photos/articles/mare-victor-sauvc/` |
| Kehadiran Kecerdasan Buatan dan Robot dalam Dunia Perang Berdasarkan Analisis Anime Eighty-Six | `assets/photos/articles/ai-robot-eighty-six/` |

## Alt text dan caption opsional

Tanpa metadata, alt text memakai nama entri. Untuk keterangan lebih jelas, buat `metadata.json` di folder foto yang sama:

```json
{
  "00-cover.jpg": {
    "alt": "ROV PEMALOE saat proses perakitan",
    "caption": "Perakitan dan integrasi sensor."
  },
  "01-proses.jpg": {
    "alt": "Pemeriksaan sambungan kabel ROV",
    "caption": "Pengecekan sebelum pengujian."
  }
}
```

Nama key harus sama persis dengan nama file foto, termasuk ekstensi dan huruf besar/kecil. Caption hanya tampil jika diisi. Metadata tidak ikut menjadi halaman publik; alt dan caption yang digunakan saja yang dimasukkan ke data situs.
