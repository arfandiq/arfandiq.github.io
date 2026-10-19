# Hasil pemeriksaan final

Diperiksa pada 19 Oktober 2026.

## Konten

- Audit sumber lulus untuk 29 nama dan teks detail lengkap entri CV, 42 bullet tanggung jawab, Professional Summary, seluruh skills, dan pendidikan.
- Tepat 3 featured projects dan 5 link artikel asli.
- Nomor telepon tidak ada pada HTML website maupun CV publik.
- Quote memiliki petik pembuka dan penutup.
- Tidak ada ilustrasi SVG, foto buatan, atau placeholder foto di halaman.

## Build dan foto

`build.py --output _site`, `check.py`, `audit_cv.py`, dan empat tes dalam `test_build.py` lulus.

Tes folder foto memakai salinan sementara, bukan folder milik pengguna: penambahan, natural sorting, nama dengan spasi, metadata alt/caption, penghapusan foto, proyek baru, id duplikat, dan batas direktori.

Semua path lokal pada HTML hasil deploy ditemukan. Isi deploy tidak menyertakan docs, data sumber, skrip, atau workflow. Sintaks kedua file JavaScript lulus pemeriksaan Node.

## Browser

- Halaman final terbuka pada http://localhost:4174/.
- Hasil build juga dibuka pada path subfolder `/_site/`, dengan 3 featured projects, 5 artikel, dan full summary terbaca.
- Dialog PEMALOE menampilkan teks lengkap, termasuk rencana evaluasi ATE-RMSE.
- Dialog instruktur Sekolah Robot Indonesia memuat kelima tanggung jawab; detail Garuda Sakti memuat empat poin.
- Pencarian Whisper menghasilkan satu proyek yang sesuai.
- Menu mobile dapat dibuka dan ditutup dengan keyboard.
- Pemeriksaan lebar desktop dan mobile tidak menemukan horizontal overflow; folder media kosong menghasilkan nol galeri.
- Screenshot desktop dan mobile tersedia di folder docs.

## Batas verifikasi

GitHub Actions belum dijalankan pada repository pengguna karena repository/remote belum dihubungkan. Konfigurasi deploy mengikuti dokumentasi GitHub Pages dan masih membutuhkan pengaturan Source = GitHub Actions satu kali di akun pengguna.

Foto asli belum diberikan, sehingga verifikasi penemuan file foto menggunakan fixture sementara. Rendering tanpa foto sudah diperiksa. Dua halaman artikel FTMM belum dapat diambil; catatannya ada di SUMBER-DAN-VERIFIKASI.md.
