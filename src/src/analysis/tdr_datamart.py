import pandas as pd
from sqlalchemy import create_engine

# Koneksi DB
engine = create_engine('mysql+pymysql://root:''@localhost/fraud_db')

# STEP 1: Load hanya kolom yang dibutuhkan untuk filter (ringan RAM)
query_filter = """
SELECT message_id, received_time, source_addr, destination_addr, network 
FROM fact_table
WHERE network IN ('Telkomsel', 'Telkomcel')
"""
df_filter = pd.read_sql(query_filter, engine)

# Pastikan datetime
df_filter['received_time'] = pd.to_datetime(df_filter['received_time'], errors='coerce')
df_filter['hour'] = df_filter['received_time'].dt.floor('h')

# ====================
# RULE 1: Repeated B#
# ====================
rule1_df = df_filter.groupby(['hour', 'destination_addr', 'network']).filter(lambda x: len(x) > 10)

# ===============================
# RULE 2: Repeated B# per SenderID
# ===============================
rule2_df = df_filter.groupby(['hour', 'source_addr', 'destination_addr', 'network']).filter(lambda x: len(x) > 10)

# Gabungkan message_id hasil rule 1 & rule 2
fraud_message_ids = pd.concat([rule1_df, rule2_df], ignore_index=True)['message_id']

# STEP 2: Ambil full row dengan semua kolom, hanya untuk message_id yang lolos rule
query_all = f"""
SELECT 
  received_time,
  substr(received_time,6,2) AS bulan,
  substr(received_time,9,2) AS tanggal,
  CEIL(DAY(received_time) / 7) AS minggu_ke,
  substr(received_time,12,2) AS jam,
  destination_addr,
  source_addr,
  network,
  dlr_status,
  COUNT(1) AS total_message
FROM fact_table
WHERE message_id IN ({','.join(f"'{mid}'" for mid in fraud_message_ids)})
GROUP BY 
  received_time,
  substr(received_time,6,2),
  substr(received_time,9,2),
  CEIL(DAY(received_time) / 7),
  substr(received_time,12,2),
  destination_addr,
  source_addr,
  network,
  dlr_status;
"""
datamart_df = pd.read_sql(query_all, engine)

# Simpan ke tabel datamart baru di DB
datamart_df.to_sql(
    "tdr_datamart_fraud",
    con=engine,
    index=False,
    if_exists='append',
    chunksize=1000
)
print("✅ Data berhasil disimpan ke MySQL")

# # Simpan ke CSV
# datamart_df.to_csv("tdr_datamart_fraud.csv", index=False, encoding='utf-8-sig')

# Simpan ke excel
datamart_df.to_excel("tdr_datamart_fraud.xlsx", index=False)
