# Edit konten tanpa membongkar layout

Semua teks detail ada di JSON terpisah dalam `data/`. Urutan dalam array menentukan urutan tampil, kecuali featured projects yang mengikuti `featuredOrder`.

## Perbedaan ringkasan dan detail

- `title`: nama lengkap yang terlihat pada kartu, arsip, dan dialog.
- `summary`: ringkasan kartu utama.
- `paragraphs`: array paragraf lengkap dalam detail dan CV publik.
- `bullets`: array semua tanggung jawab atau poin kontribusi dalam detail dan CV publik.
- `date`: tanggal tampilan, misalnya `01/2026 - Present`.
- `org`: organisasi/perusahaan, digunakan pada pengalaman dan penghargaan.
- `location`: lokasi jika relevan.
- `id`: identitas unik di seluruh file. Gunakan huruf kecil, angka, dan tanda hubung.
- `photoFolder`: folder foto dari root situs, harus dalam `assets/photos/`.

## Tambah proyek

Salin satu objek dalam `data/projects.json`, tempel sebelum kurung siku terakhir, lalu ganti semua kontennya. Contoh:

```json
{
  "id": "nama-proyek-baru",
  "title": "Nama lengkap proyek baru",
  "date": "11/2026 - Present",
  "category": "Embedded systems",
  "summary": "Ringkasan yang menjelaskan tujuan proyek.",
  "paragraphs": [
    "Penjelasan lengkap tentang proyek, tujuan, lingkup, dan kontribusi.",
    "Paragraf tambahan tentang metode, teknologi, dan hasil jika tersedia."
  ],
  "bullets": [
    "Kontribusi atau tanggung jawab pertama.",
    "Kontribusi atau tanggung jawab kedua."
  ],
  "photoFolder": "assets/photos/projects/nama-proyek-baru",
  "featured": false,
  "featuredOrder": 0,
  "tags": ["Arduino", "Python"]
}
```

Buat folder foto sesuai `photoFolder`. Build juga dapat membuat folder baru ini secara otomatis. Jumlah proyek dan opsi filter mengikuti data secara otomatis.

## Ganti featured projects

Tetapkan `featured: true` pada tepat tiga proyek. Isi `featuredOrder` dengan 1, 2, dan 3. Proyek lain memakai `false` dan 0. Build memberi pesan kesalahan jika jumlah featured bukan tiga, supaya pilihan desain tidak berubah tanpa sengaja.

## Tambah kerja, internship, organisasi, atau penghargaan

Salin objek pada file kategori yang sesuai. Ganti `id`, `title`, `org`, `date`, `summary`, `paragraphs`, `bullets`, dan `photoFolder`. Tidak perlu `category`, `featured`, `featuredOrder`, atau `tags` untuk entri selain proyek. Jumlah tab ikut berubah otomatis.

## Tambah artikel

Pada `data/articles.json`, salin entri dan gunakan `id` unik, judul asli, penerbit, `description` singkat, `url` HTTPS asli, serta `photoFolder`. `date` opsional. `kind` bisa `Feature` atau `Article by Arfandi Qurrataain` jika memang tulisan sendiri. Tidak perlu menambahkan `paragraphs` atau `bullets` untuk artikel; kartu membuka situs sumber langsung.

## Profil dan pendidikan

Edit `data/profile.json`. Semua skill dalam `skills` tetap tampil. Skill yang bukan ROS/Python/C/C++ masuk kelompok People & process; ubah pengelompokan dalam `assets/js/site.js` jika ingin menambah disiplin teknis baru. `tools` berdiri sendiri. Pendidikan tetap memakai S.T. dengan status in progress sampai lo secara sengaja memperbaruinya setelah lulus.

`heroTitle` adalah array baris judul pembuka. Baris terakhir memakai aksen orange. `quote.text` berisi kalimat kutipan tanpa tanda petik dekoratif, karena petik pembuka dan penutup sudah ditangani tampilan.

## Setelah mengedit

Preview: `python3 scripts/preview.py`. Untuk build saja: `python3 scripts/build.py`. Untuk siap deploy: `python3 scripts/build.py --output _site`.

Jangan mengedit `assets/js/content.js` dan `cv.html` langsung karena akan tertimpa build. Perubahan data tetap harus di-commit dan push agar versi GitHub Pages berubah.

## Sosmed dan pesan anonim

Edit `socials` dalam `data/profile.json` untuk menambah atau mengganti akun. Setiap entri berisi `name`, `handle`, dan `url` HTTPS. Empat akun awal: TikTok, Instagram, X, dan YouTube. `anonymousMessage` berisi `label` dan `url` NGL, ditampilkan sebagai tombol terpisah. Semua tautan membuka tab baru.
