# 📊 Telecom SMS Fraud Detection System

This repository contains a **near real-time SMS fraud detection system** developed as part of an internship (Kerja Praktik). The system analyzes **SMS CDR (Call Detail Record) data**, focusing specifically on SMS traffic patterns to identify **suspicious or abnormal behavior** that may indicate fraud.

The implementation uses a **modular, script-based pipeline**, where each processing stage is executed independently and each script can be run separately based on the processing needs.

---

## 🎯 Project Objectives

* Analyze SMS CDR data (SMS only, not voice calls)
* Perform automated data cleansing from raw CSV files
* Detect suspicious SMS traffic patterns
* Store processed data into a relational database
* Visualize fraud indicators using Tableau dashboards

---

## 🧠 What Is Considered Suspicious SMS Activity?

Suspicious SMS activity is identified based on **traffic patterns**, not message content. Examples include:

* Extremely high SMS volume from a single sender within a short time window
* Repeated SMS delivery to the same destination number
* Sudden traffic spikes compared to normal or historical behavior
* SMS activity occurring at unusual hours (e.g., late night)
* Newly observed senders generating abnormal traffic immediately

Such patterns may indicate **artificial or automated SMS traffic**, which can be exploited for financial gain through SMS billing or interconnection mechanisms.

---

## ⚙️ System Characteristics

* **Processing type**: Near real-time (file-based monitoring)
* **Input data**: SMS CDR CSV files
* **Execution model**: Script-based (run per module)
* **Database**: MySQL (managed via phpMyAdmin)
* **Visualization**: Tableau

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* MySQL
* phpMyAdmin
* Tableau
* Linux / Windows

---

## 🏗️ Project Structure

```
telecom-sms-fraud-detection/
│
├── src/
│   ├── parser/
│   │   └── sms_parser.py      # CSV parsing, cleansing, table creation, DB insert
│   │
│   └── analysis/
│       └── fraud_scoring.py   # Rule-based fraud analysis & scoring
│
├── visualization/
│   └── tableau/
│       └── sms_fraud_dashboard.twbx
│
├── data/
│   └── sample_sms_cdr.csv     # Sample / dummy data
│
├── export/
│   └── fraud_output_sample.csv
│
├── src/docs/
│   ├── System_Frames_Architecture.png
│   ├── Fraud_Rule_Concept.png
│   ├── Database_Table.png
│   └── Tableau_Preview.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 System Workflow

1. SMS CDR CSV files are placed in the input directory
2. Parsing script reads and cleanses SMS records
3. Database tables are created automatically if not present
4. Cleaned data is inserted into the database
5. Fraud rules are applied to identify suspicious behavior
6. Aggregated results are exported to CSV
7. Tableau dashboard visualizes fraud patterns and trends

---

## 📐 System Architecture

![System Architecture](src/docs/System_Frames_Architecture.png)

---

## ▶️ How to Run

Each module can be executed independently depending on the processing stage.

### 1️⃣ Run CSV Parsing & Cleansing

```bash
python src/parser/sms_parser.py
```

### 2️⃣ Run Fraud Analysis

```bash
python src/analysis/fraud_scoring.py
```

---

## 🧠 Fraud Detection Logic (Conceptual)

The fraud detection logic is **rule-based** and focuses on identifying abnormal SMS traffic patterns such as:

* High-frequency SMS bursts
* Repeated sender–receiver interactions
* Time-window based volume anomalies

All rules and thresholds shown are **simplified and anonymized** for portfolio demonstration purposes.

![Fraud Rule Concept](src/docs/Fraud_Rule_Concept.png)

---

## 🗄️ Database Output

Processed and cleansed SMS data is stored in a MySQL database. Tables are created automatically by the parsing script.

![Database Table](src/docs/Database_Table.png)

---

## 📊 Visualization (Tableau)

Fraud indicators and traffic patterns are visualized using Tableau dashboards to support monitoring and analysis.

![Tableau Dashboard](src/docs/Tableau_Preview.png)

Tableau workbook files are located in:

```
visualization/tableau/
```

---

## 🔐 Disclaimer

> The architecture, fraud rules, and visual materials in this repository are simplified and anonymized.
> This project does not contain proprietary systems, confidential parameters, or production-level fraud logic.

---

## 📌 Use Cases

* SMS traffic monitoring and analysis
* Fraud pattern detection demonstration
* Internship / academic portfolio

---

## 👤 Author

**Zarvin PW**
Internship (Kerja Praktik) Project – Telecom SMS Fraud Detection System
