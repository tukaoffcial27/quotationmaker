import pandas as pd
import os
import shutil

# 1. Konfigurasi Dasar Project Quotation
base_url = "https://quotationmaker.guidify.app" 
output_dir = "public/layanan"

# Reset folder public agar bersih setiap kali build
if os.path.exists('public'): 
    shutil.rmtree('public')
os.makedirs(output_dir, exist_ok=True)

# 2. Load Data & Template
if not os.path.exists('database_pseo.csv'):
    print("❌ Error: database_pseo.csv tidak ditemukan! Jalankan generate_database.py dulu.")
    exit()

df = pd.read_csv('database_pseo.csv')
if not os.path.exists('template.html'):
    print("❌ Error: template.html tidak ditemukan!")
    exit()

with open('template.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

sitemap_urls = []

print(f"🚀 Memproses {len(df)} data untuk sitemap dan halaman statis Quotation...")

# 3. Looping Pembuatan Halaman
for index, row in df.iterrows():
    # Logika slug: prof_slug-city_slug
    p_slug = str(row['prof_slug'])
    c_slug = str(row['city_slug'])
    current_slug = f"{p_slug}-{c_slug}"
    
    url = f"{base_url}/layanan/{current_slug}"
    sitemap_urls.append(url)
    
    # Generate 200 Halaman Statis Pertama untuk mempercepat Vercel
    if index < 200:
        content = template_content
        for col in df.columns:
            placeholder = f"{{{{{col}}}}}"
            content = content.replace(placeholder, str(row[col]))
        
        with open(f"{output_dir}/{current_slug}.html", "w", encoding='utf-8') as f:
            f.write(content)

# 4. Pembuatan Sitemap dengan Perbaikan Ampersand (&)
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
# Tambahkan URL Utama (Homepage)
sitemap_content += f'  <url><loc>{base_url}/</loc><priority>1.0</priority></url>\n'

for loc in sitemap_urls:
    # Mengamankan karakter & agar XML tidak error
    safe_loc = loc.replace("&", "&amp;")
    sitemap_content += f'  <url><loc>{safe_loc}</loc></url>\n'

sitemap_content += '</urlset>'

with open("public/sitemap.xml", "w", encoding='utf-8') as f:
    f.write(sitemap_content)

# 5. Salin Aset Statis ke Folder Public
# Fokus pada 3 foto baru: preview-quotation
files_to_copy = [
    'index.html', 
    'robots.txt', 
    'preview-quotation.jpg',
    'preview-quotation1.jpg',
    'preview-quotation2.jpg'
]

for file_name in files_to_copy:
    if os.path.exists(file_name):
        shutil.copy(file_name, f"public/{file_name}")
        print(f"✅ Berhasil menyalin: {file_name}")
    else:
        print(f"⚠️ Peringatan: {file_name} tidak ditemukan di folder root.")

print(f"✅ SUKSES! Proyek Quotation siap di-deploy.")