# Publish ke GitHub Pages

## 1. Pilih nama repository

- Alamat utama: buat repository bernama **USERNAME.github.io**, dengan USERNAME sesuai username GitHub yang sebenarnya.
- Alamat proyek: nama repository bebas, misalnya `portfolio`, hasilnya **https://USERNAME.github.io/portfolio/**.
- Branding ARFANDIQA tidak harus sama dengan username GitHub. Jangan menebak username berdasarkan nama folder komputer.

Gunakan repository public jika memakai GitHub Free untuk Pages. Petunjuk resmi: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## 2. Masukkan isi PORTOFIXED ke root repository

Root repository harus langsung berisi `index.html`, `data/`, `assets/`, `scripts/`, dan `.github/`. Jangan membungkus seluruh situs satu tingkat lagi dalam folder PORTOFIXED di repository.

Kalau membuat repository baru, buat kosong agar langkah awal sederhana. Contoh dari terminal dalam PORTOFIXED:

```bash
git init
git branch -M main
git add .
git commit -m "Publish ARFANDIQA website"
git remote add origin https://github.com/USERNAME/NAMA-REPO.git
git push -u origin main
```

Ganti USERNAME dan NAMA-REPO dengan repository lo. Login menggunakan mekanisme GitHub yang tersedia di komputer. Jangan masukkan password/token ke file website.

Kalau repository sudah di-clone, salin isi folder ini termasuk folder tersembunyi `.github`, lalu commit dan push dari checkout tersebut. Jangan jalankan `git remote add` lagi jika remote sudah ada.

## 3. Aktifkan Pages satu kali

Di repository: **Settings → Pages → Build and deployment → Source → GitHub Actions**.

Buka tab **Actions**. Pilih **Build and deploy ARFANDIQA**. Jika push pertama terjadi sebelum Pages aktif, klik **Run workflow** atau jalankan ulang workflow yang gagal setelah pengaturan di atas selesai.

Workflow otomatis berjalan pada push ke `main` atau `master`. Jika lo menggunakan branch lain, ubah daftar branch di `.github/workflows/pages.yml`. Repository root dan project sites sama-sama didukung oleh path relatif.

## 4. Update setelah live

1. Edit file JSON atau taruh foto asli di folder yang sesuai.
2. Preview lokal jika perlu.
3. Commit dan push.
4. Tunggu build serta deploy berwarna hijau di Actions.
5. Refresh website; gunakan hard refresh jika browser menampilkan versi lama.

Tidak perlu menjalankan build di komputer sebelum push. GitHub Actions menjalankannya otomatis. Git tidak menyimpan folder kosong, jadi setiap folder foto sudah memiliki README yang menjaganya tetap tersedia di repository.

## Jika gagal

- JSON error: cek tanda petik dua dan koma, lalu jalankan `python3 scripts/build.py` untuk melihat file yang bermasalah.
- Foto tidak muncul: cek ekstensi yang didukung, folder pada `photoFolder`, dan pastikan foto sudah ikut commit. Nama huruf besar/kecil harus sesuai.
- Pages 404: pastikan Source = GitHub Actions, deployment sukses, dan buka URL yang ditampilkan pada deployment.
- Workflow tidak berjalan: pastikan file `.github/workflows/pages.yml` ikut di-push dan branch adalah `main` atau `master`.
- Izin environment: jika lo menambahkan aturan approval di environment `github-pages`, deployment menunggu approval yang lo tetapkan.
- Build lokal gagal karena Python tidak ditemukan: pasang Python 3.10+ atau gunakan build GitHub Actions. Tidak ada paket Python tambahan yang perlu di-install.

File ini belum mem-push atau menerbitkan apa pun ke akun GitHub. URL live akan tersedia setelah repository dan pengaturan Pages dibuat di akun lo.
