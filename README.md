# 📊 SMS Fraud Detection System

This project is a **near real-time SMS fraud detection system** designed to monitor and analyze telecom SMS activity by processing periodically generated **SMS CDR (Short Message Service Call Detail Record) CSV files**.

The system focuses on **data cleansing, fraud risk scoring, anomaly detection, and aggregation**, with results stored in a local database and visualized using **Tableau dashboards**.

---

## 🎯 Project Objectives

* Detect suspicious and potentially fraudulent SMS activity
* Perform automated data cleansing and validation
* Generate fraud risk scores for SMS traffic
* Support fraud monitoring through analytical dashboards

---

## ⚙️ System Characteristics

* **Processing type**: Near real-time (scheduled / file-based)
* **Input**: Periodic SMS CDR CSV files
* **Processing engine**: Python scripts
* **Storage**: Local database (SQLite / MySQL)
* **Visualization**: Tableau

> This system does **not** use streaming platforms (Kafka, Spark, Hive). It is designed for efficient scheduled processing and monitoring.

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* SQLite / MySQL
* Tableau (for visualization)
* Linux / Windows

---

## 🏗️ Project Structure

```
sms-fraud-detection-system/
│
├── src/                    # Main processing logic
│   ├── main.py             # Entry point
│   ├── parser/             # CSV parsing & cleansing
│   ├── analysis/           # Risk scoring & anomaly detection
│   └── database/           # Database handler
│
├── visualization/
│   └── tableau/            # Tableau dashboard files
│
├── data/
│   └── sample_sms_cdr.csv  # Sample dataset (dummy data)
│
├── docs/                   # Documentation & screenshots
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 System Workflow

1. SMS CDR CSV files are generated periodically
2. Python parser processes and cleans incoming data
3. Fraud risk scoring and anomaly detection are applied
4. Results are stored in a local database
5. Aggregated outputs are exported for visualization
6. Tableau dashboard displays fraud metrics and trends

---

## 📊 Visualization (Tableau)

The fraud analysis results are visualized using **Tableau**, including:

* Fraud risk score distribution
* Top suspicious MSISDN
* Time-based SMS fraud trends

📁 Tableau files are located in:

```
visualization/tableau/
```

A dashboard preview image is available in the `docs/` folder.

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the main processing script:

```bash
python src/main.py
```

3. Open the Tableau dashboard:

* Install Tableau Public or Tableau Desktop
* Open the `.twbx` file inside `visualization/tableau/`

---

## 📌 Use Cases

* Telecom fraud monitoring
* SMS spam analysis
* Near real-time data analytics
* Internship / academic project portfolio

---

## 🚀 Future Improvements

* Integration with streaming platforms (Kafka / Spark)
* Real-time alerting system
* Web-based dashboard
* Advanced machine learning models

---

## 👤 Author

**Zarvin Heruwin*
Internship Project – SMS Fraud Analytics
