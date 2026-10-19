# ARFANDIQA

Versi final website Ocean-Tech Editorial untuk GitHub Pages. Semua file yang perlu masuk repository ada di folder ini, termasuk `.github`. Tidak perlu framework, npm, atau layanan berbayar.

## Mulai dari sini

1. Baca [panduan upload GitHub Pages](docs/PUBLISH-GITHUB-PAGES.md).
2. Taruh foto profil di `assets/photos/profile/`.
3. Taruh foto proyek/pengalaman ke folder yang sesuai dalam `assets/photos/`. Lihat [peta folder foto](docs/PANDUAN-FOTO.md).
4. Commit dan push ke `main` atau `master`. GitHub Actions membaca folder foto, membangun situs, lalu menerbitkan pembaruan.

**Pengaturan satu kali di GitHub diperlukan:** Settings → Pages → Build and deployment → Source → GitHub Actions. Setelah itu, pembaruan lewat push akan otomatis diproses.

## Preview di komputer

Dari folder PORTOFIXED:

```bash
python3 scripts/preview.py
```

Buka http://localhost:4174. Setelah menaruh foto atau mengubah data, tunggu pesan `Content/photos updated`, lalu refresh browser. Hentikan dengan Ctrl+C. Untuk port lain: `python3 scripts/preview.py --port 4180`.

`index.html` juga bisa langsung dibuka. Jika baru mengedit data/foto, jalankan `python3 scripts/build.py` dulu agar file tampilan diperbarui. Browser tidak dapat membaca daftar folder foto sendiri; proses build lokal atau GitHub Actions yang melakukannya.

## File yang biasanya diedit

| Keperluan | File/folder |
| --- | --- |
| Identitas, pengantar, pendidikan, skill, tools, quote | `data/profile.json` |
| Proyek dan tiga featured projects | `data/projects.json` |
| Pengalaman kerja | `data/work.json` |
| Internship | `data/internship.json` |
| Organisasi | `data/organization.json` |
| Penghargaan | `data/awards.json` |
| Articles & Features | `data/articles.json` |
| Foto asli | `assets/photos/` |
| Warna, tekstur, ukuran, layout | `assets/css/style.css` |
| Struktur utama halaman | `index.html` |
| Interaksi website | `assets/js/site.js` |
| Otomatisasi GitHub Pages | `.github/workflows/pages.yml` |

**Jangan edit `assets/js/content.js` atau `cv.html` langsung.** Keduanya dibuat ulang dari `data/` saat build. File JSON menggunakan tanda petik dua, tanpa komentar atau koma terakhir.

Panduan lanjut: [edit konten dan tambah entri](docs/PANDUAN-EDIT.md) · [foto dan caption](docs/PANDUAN-FOTO.md) · [catatan sumber](docs/SUMBER-DAN-VERIFIKASI.md).

## Isi final

- 13 proyek, dengan tepat tiga featured projects sesuai pilihan.
- 2 pengalaman kerja, 1 internship, 8 pengalaman organisasi, 5 penghargaan.
- Semua 29 nama dan detail entri sesuai CV, termasuk 42 butir tanggung jawab. Ringkasan ada di kartu; teks lengkap tampil di detail.
- Professional Summary, pendidikan, skills, dan semua tools yang diminta.
- S.T. berstatus masih berjalan, bukan gelar yang telah diperoleh.
- Lima link artikel asli, quote dengan petik pembuka dan penutup, tanpa nomor telepon di halaman maupun versi CV publik.
- Foto profil dan desain asli pada folder terpisah; galeri opsional untuk setiap entri. Folder kosong tidak memunculkan kotak kosong.
- Pencarian dan filter proyek, navigasi mobile, tab keyboard, dialog dengan Escape dan pengembalian fokus, animasi, reduced-motion, tekstur CSS tanpa ilustrasi.
- CV lengkap di `cv.html`, dapat dicetak atau disimpan sebagai PDF menggunakan tombol **Print / Save PDF**.

## Pemeriksaan

```bash
python3 scripts/build.py --output _site
python3 scripts/check.py
python3 scripts/test_build.py
```

Pemeriksaan sumber awal CV (wajar berubah setelah lo sengaja memperbarui isi):

```bash
python3 scripts/audit_cv.py
```

`_site/` adalah hasil siap hosting. GitHub Actions hanya mengunggah hasil ini, bukan panduan, sumber data, atau skrip. Link aset relatif mendukung alamat `USERNAME.github.io` maupun `USERNAME.github.io/NAMA-REPO/`.

Font Google Fonts opsional; sistem memakai font bawaan kalau offline. Website tetap dapat dibuka tanpa koneksi setelah file tersedia lokal, kecuali link artikel dan akun eksternal.
