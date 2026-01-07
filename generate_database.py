import json
import csv
import random
import os

def generate_database():
    # Pastikan file cities.json ada sebelum diproses
    if not os.path.exists('cities.json'):
        print("❌ Error: File cities.json tidak ditemukan!")
        return

    with open('cities.json', 'r', encoding='utf-8') as f:
        cities_data = json.load(f)

    # Nama foto utama untuk project Quotation Maker
    product_img = "preview-quotation.jpg"

    # Daftar Profesi/Bisnis yang sering membutuhkan Quotation Profesional
    matrix_professions = [
        "Kontraktor Bangunan", "Interior Designer", "Freelance Graphic Designer", 
        "Web Developer", "Wedding Organizer", "Catering Service", 
        "Jasa Fotografi", "Konsultan Bisnis", "Supplier Material", 
        "Bengkel Las", "Toko Furnitur", "Jasa Kebersihan", 
        "IT Support", "Event Organizer", "Jasa Arsitek", 
        "Digital Agency", "Distributor Barang", "Jasa Renovasi", 
        "Rental Mobil", "Layanan Service AC"
    ]

    # Masalah nyata dalam pembuatan Quotation (Pain Points)
    pains = [
        "repot hitung PPN 11% secara manual yang sering salah",
        "tampilan penawaran harga tidak profesional dan meragukan",
        "bingung menyusun deskripsi item yang rapi dan terstruktur",
        "lama membuat revisi harga karena harus ketik ulang dari awal",
        "penawaran harga sering diabaikan klien karena format berantakan"
    ]

    # Dampak buruk jika Quotation buruk (Business Losses)
    losses = [
        "kehilangan tender proyek besar karena dokumen tidak bonafid",
        "kerugian finansial akibat salah hitung kalkulasi pajak",
        "kredibilitas perusahaan dipertanyakan oleh calon investor",
        "proses closing tertunda lama karena administrasi lambat",
        "buang-buang waktu hanya untuk urusan desain dokumen"
    ]

    prefix_titles = ["Contoh", "Template", "Aplikasi", "Download", "Format", "Jasa Pembuat", "Tutorial", "Cara Buat"]
    suffix_titles = ["Profesional", "Terbaik", "Siap Pakai", "Otomatis PPN", "Versi PDF A4", "Format Eksekutif"]

    # Membuat file database_pseo.csv
    with open('database_pseo.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header kolom tetap sama agar sistem generate_pages & index.py tidak perlu berubah logikanya
        writer.writerow(['city', 'city_slug', 'profession', 'prof_slug', 'category', 'pain_point', 'business_loss', 'product_image', 'title_page', 'h1_header'])
        
        for prof_name in matrix_professions:
            for c in cities_data:
                # Membuat slug untuk profesi
                prof_slug = prof_name.lower().replace(" ", "-")
                
                # Menyusun Judul Halaman dan Header
                t_page = f"{random.choice(prefix_titles)} Quotation {prof_name} di {c['city']} {random.choice(suffix_titles)}"
                h1_head = f"Buat Penawaran Harga {prof_name} {c['city']} Lebih Profesional"
                
                writer.writerow([
                    c['city'], 
                    c['slug'], 
                    prof_name, 
                    prof_slug, 
                    "Bisnis", 
                    random.choice(pains), 
                    random.choice(losses), 
                    product_img, 
                    t_page, 
                    h1_head
                ])

    print(f"✨ Sukses! {len(matrix_professions) * len(cities_data)} baris data Quotation telah dibuat di database_pseo.csv")

if __name__ == "__main__":
    generate_database()