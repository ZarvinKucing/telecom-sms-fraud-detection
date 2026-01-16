import os #	Mengelola file dan direktori.
import shutil # Memindahkan file antar folder.
import pandas as pd # Membaca file CSV, manipulasi data, dan menyimpan ke database.
from glob import glob # Mengambil file
from time import time # Mengukur durasi eksekusi script
from datetime import datetime, timedelta # 	Mengubah/menghitung waktu dengan format
from sqlalchemy import create_engine # Menghubungkan Python ke MySQL menggunakan SQLAlchemy engine.
from sqlalchemy.exc import SQLAlchemyError # Menangkap error saat penyimpanan ke MySQL.

# === Mulai stopwatch ===
start_time = time()

# === Setup direktori ===
data_dir = "./data_tdr"
processed_dir = "./parsed"
os.makedirs(processed_dir, exist_ok=True)

# === Ambil semua file CSV pakai glob ===
file_list = glob(os.path.join(data_dir, "*.csv")) # Mencari semua file .csv di folder ./data_tdr

# === Koneksi database ===
engine = create_engine('mysql+pymysql://root:''@localhost/fraud_db')

# === Proses semua file ===
all_dfs = []
total_rows = 0
processed_count = 0
deleted_count = 0

print(f"🔄 Memulai pemrosesan {len(file_list)} file CSV...\n")

for filepath in file_list: # Proses satu per satu file dari list CSV
    filename = os.path.basename(filepath) # Ambil nama file dari path lengkap.
    print(f"📄 Membaca: {filename}")
    
    # Cek apakah file sudah ada di folder done sebelum memproses
    destination_file = os.path.join(processed_dir, filename)
    if os.path.exists(destination_file):
        print(f"   🗑️ File sudah ada di folder done - DIHAPUS")
        os.remove(filepath)  # Jika file sudah ada di folder parsed, file input terhapus agar tidak duplikat.
        deleted_count += 1
        print(f"   ✅ File berhasil dihapus\n")
        continue
    
    try:
        df = pd.read_csv(filepath)
        row_count = len(df)  # Baca file CSV jadi DataFrame df, hitung jumlah barisnya.
        total_rows += row_count
        processed_count += 1
        
        print(f"   ✅ Berhasil - {row_count:,} baris")

        # Konversi kolom yang berpotensi terlalu panjang ke string dan truncate jika perlu
        if 'destination_addr' in df.columns:
            df['destination_addr'] = df['destination_addr'].astype(str)
            # Batasi panjang destination_addr (sesuaikan dengan schema MySQL Anda)
            df['destination_addr'] = df['destination_addr'].str[:50]  # Maksimal 20 karakter
            
        if 'source_addr' in df.columns:
            df['source_addr'] = df['source_addr'].astype(str)
            df['source_addr'] = df['source_addr'].str[:50]  # Maksimal 20 karakter
            
        all_dfs.append(df)

        # Pindahkan file ke folder parsed
        shutil.move(filepath, destination_file)
        print(f"   📁 Dipindahkan ke folder parsed\n")

    except Exception as e:
        print(f"   ❌ Gagal memproses: {e}\n")

# === Simpan ke MySQL dengan batch/chunksize ===
print("=" * 50)
print("📊 RINGKASAN PEMROSESAN")
print("=" * 50)
print(f"📁 Total file ditemukan: {len(file_list)}")
print(f"✅ File berhasil diproses: {processed_count}")
print(f"🗑️ File dihapus (sudah ada): {deleted_count}")
print(f"❌ File gagal diproses: {len(file_list) - processed_count - deleted_count}")
print(f"📊 Total baris data: {total_rows:,}")
print(f"📊 Rata-rata baris per file: {total_rows//processed_count if processed_count > 0 else 0:,}")
print("=" * 50)

if all_dfs:
    final_df = pd.concat(all_dfs, ignore_index=True)
    print(f"\n💾 Menyimpan {len(final_df):,} baris ke MySQL secara batch...")
    try:
        # Simpan ke MySQL dalam batch (misal 20.000 baris per batch)
        batch_size = 50000
        total_batches = (len(final_df) + batch_size - 1) // batch_size

        for i in range(0, len(final_df), batch_size):
            chunk = final_df.iloc[i:i+batch_size]
            connection = engine.connect()
            transaction = connection.begin()

            # chunk.to_sql('fact_table', con=engine, if_exists='append' if i > 0 else 'replace', index=False)
            chunk.to_sql('fact_table', con=engine, if_exists='append', index=False)

            transaction.commit()
            
            print(f"   🚚 Batch {i//batch_size+1}/{total_batches} ({len(chunk)} baris) berhasil di-load.")
        print("✅ Semua data berhasil disimpan ke MySQL.")
    
    except SQLAlchemyError as e:
        print("❌ Error saat menyimpan ke MySQL:")
        print(e)

    finally:
        connection.close()
        engine.dispose()

else:
    print("⚠️ Tidak ada file CSV yang diproses.")

# === Akhiri stopwatch ===
end_time = time()
elapsed = end_time - start_time
print(f"\n⏱️ Waktu eksekusi: {elapsed:.2f} detik ({str(timedelta(seconds=int(elapsed)))})")
