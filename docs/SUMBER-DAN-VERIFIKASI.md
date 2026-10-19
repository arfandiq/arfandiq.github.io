# Sumber dan catatan final

Konten utama berasal dari Arfandi_Qurrataain_FlowCV_Resume_2026-10-19(1).pdf. Salinan teks untuk audit ada di `source-cv-text.txt`, dengan header kontak pribadi dihilangkan. File audit tidak ikut deploy.

Seluruh 29 nama entri, teks penjelasan, dan 42 poin tanggung jawab diambil dari sumber asli. Baris yang terpotong akibat layout PDF disatukan. Rentang tanggal menggunakan tanda hubung biasa. Susunan skill pada halaman dapat berbeda karena pengelompokan, tetapi semua skill tetap tersedia. Ringkasan kartu merupakan ringkasan editorial; detail dan CV publik memuat teks lengkap sumber.

Ejaan asli seperti **PKM Divison Staff**, **22st place**, dan **Senior Support Programming** dipertahankan pada detail yang memuatnya karena permintaan mengikuti CV persis. Klaim ranking dan status ongoing mengikuti sumber bertanggal 19 Oktober 2026. S.T. diberi keterangan masih berlangsung dan belum diberikan.

Nomor telepon tidak disertakan di website atau CV publik. CV publik dibuat dari data lengkap sebagai `cv.html`; pengunjung dapat memilih Print / Save PDF. PDF sumber di folder induk tidak diubah atau diunggah sebagai aset publik.

PDF engineering portfolio dan foto asli belum tersedia saat finalisasi. Tidak ada foto stok, ilustrasi generatif, atau diagram rekaan. Slot media hanya muncul ketika foto asli tersedia. Desain grid, titik, dan garis diagonal dibuat menggunakan CSS.

## Artikel

Lima URL yang diberikan pemilik sudah dimasukkan. Judul, tanggal, dan ringkasan kedua artikel UNAIR NEWS serta tulisan Retizen berhasil dibaca dari halaman aslinya. Dua halaman FTMM tidak dapat diambil pada pemeriksaan ini; judul mengikuti slug URL, tanggal tidak ditebak, dan ringkasannya hanya menjelaskan topik dari link. Catatan tersebut juga tersimpan pada entri terkait dalam `data/articles.json`.

Tulisan Retizen bertema Eighty-Six dimasukkan karena diminta khusus oleh pemilik. Artikel tidak mengubah identitas profesional atau menambahkan kategori minat pribadi.

Quote dan atribusi Kaela Kovalskia berasal dari teks yang diberikan pemilik, dengan petik penutup ditambahkan sesuai persetujuan.

## Pemeriksaan yang disediakan

- `scripts/audit_cv.py`: kecocokan lengkap nama, detail, jumlah bullet, summary, dan skill dengan sumber CV awal.
- `scripts/check.py`: data, link lokal, path relatif project sites, sintaks JS jika Node tersedia, nomor telepon, dan batas folder deploy.
- `scripts/test_build.py`: foto drag-and-drop, urutan, caption, nama ber-spasi, penghapusan foto, penambahan proyek, id duplikat, dan penolakan folder di luar area foto.

Panduan workflow mengikuti dokumentasi resmi GitHub Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
