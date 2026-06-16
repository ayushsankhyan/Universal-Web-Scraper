# 🌐 Universal Web Scraper & Analytics Dashboard

## 📌 Overview

Universal Web Scraper is a Python-based data extraction and analytics platform that automatically scrapes web pages, extracts structured information, stores data in PostgreSQL, and visualizes results through an interactive Streamlit dashboard.

The project combines web scraping, database management, data processing, and dashboard development into a single end-to-end application.

---

## 🚀 Features

### Web Scraping

* Scrapes data from websites using Requests and BeautifulSoup
* Handles multi-page websites through pagination
* Detects repeating content blocks automatically
* Extracts records dynamically

### Data Processing

* Automatic field detection
* Product title extraction
* Price extraction
* Stock status extraction
* CSV export functionality

### Database Integration

* PostgreSQL data storage
* Structured product records
* Queryable datasets
* Persistent storage

### Analytics Dashboard

* Interactive Streamlit dashboard
* Product search functionality
* Price filtering
* Stock filtering
* KPI metrics
* Price distribution visualization
* CSV download support

---

## 🛠️ Tech Stack

| Category        | Technologies                              |
| --------------- | ----------------------------------------- |
| Language        | Python                                    |
| Web Scraping    | Requests, BeautifulSoup, Scrapy, Selenium |
| Database        | PostgreSQL                                |
| Dashboard       | Streamlit                                 |
| Data Analysis   | Pandas                                    |
| Visualization   | Plotly                                    |
| Version Control | Git, GitHub                               |

---

## 📂 Project Structure

```text
Universal-Web-Scraper
│
├── dashboard/
│   └── app.py
│
├── scraper/
│   ├── db.py
│   ├── exporter.py
│   ├── fetcher.py
│   ├── field_detector.py
│   ├── parser.py
│   └── product_parser.py
│
├── universal_scraper/
│
├── universal_v2.py
├── requirements.txt
├── run_scraper.bat
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/ayushsankhyan/Universal-Web-Scraper.git
cd Universal-Web-Scraper
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE scraper_db;
```

Update PostgreSQL credentials inside:

```text
scraper/db.py
dashboard/app.py
```

---

## ▶️ Running the Scraper

```bash
python universal_v2.py
```

Example input:

```text
https://books.toscrape.com
```

---

## 📊 Running the Dashboard

```bash
streamlit run dashboard/app.py
```

---

## 📈 Dashboard Features

* Product Search
* Price Range Filter
* Stock Status Filter
* KPI Cards
* Price Distribution Histogram
* CSV Export
* Source Analytics

---

## 📸 Screenshots

Add screenshots in a folder named:

```text
screenshots/
```

Suggested images:

* dashboard.png
* scraper_execution.png
* postgresql_records.png

---

## 🔮 Future Enhancements

* Multi-URL scraping
* Scheduled scraping jobs
* Cloud deployment
* User authentication
* Advanced analytics
* Real-time monitoring
* API integration

---

## 👨‍💻 Author

**Ayush Sankhyan**

BE CSE (Hons) - Artificial Intelligence & Machine Learning

Chandigarh University

GitHub: https://github.com/ayushsankhyan
Mail: sankhyanayush95@gmail.com

