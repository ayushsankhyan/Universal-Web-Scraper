\# 🌐 Universal Web Scraper \& Analytics Dashboard
URL : https://universal-web-scraper-kd3bu6vkhxqqjzmcuqg2sz.streamlit.app/



A Python-based end-to-end web scraping platform that automatically extracts data from websites, stores it in PostgreSQL, and visualizes the results through an interactive Streamlit dashboard.



This project demonstrates skills in \*\*Web Scraping, Data Extraction, Data Storage, Database Management, Data Analytics, and Dashboard Development\*\*.



\---



\## 🚀 Project Overview



The Universal Web Scraper is designed to scrape structured information from websites with repeating content patterns.



The system:



1\. Fetches web pages automatically

2\. Detects repeating content blocks

3\. Extracts useful fields such as:

&#x20;  - Product Title

&#x20;  - Price

&#x20;  - Stock Status

4\. Stores records in PostgreSQL

5\. Exports data to CSV

6\. Displays insights through a Streamlit Analytics Dashboard



\---



\## 🏗️ System Architecture



```text

Website URL

&#x20;     │

&#x20;     ▼

Requests + BeautifulSoup

&#x20;     │

&#x20;     ▼

Record Detection Engine

&#x20;     │

&#x20;     ▼

Field Extraction

&#x20;     │

&#x20;     ▼

PostgreSQL Database

&#x20;     │

&#x20;     ▼

Streamlit Dashboard

&#x20;     │

&#x20;     ▼

Analytics \& Visualization

```



\---



\## ✨ Features



\### 🌍 Web Scraping



\- Automatic page fetching

\- Pagination handling

\- Dynamic record detection

\- Structured data extraction

\- Multi-record processing



\### 🔍 Field Detection



Automatically detects:



\- Product Title

\- Price

\- Stock Availability



\### 🗄️ Database Integration



\- PostgreSQL Storage

\- Persistent Data Management

\- Queryable Records

\- Structured Product Dataset



\### 📊 Analytics Dashboard



\- Interactive Dashboard

\- Product Search

\- Price Filtering

\- Stock Filtering

\- KPI Metrics

\- Price Distribution Analytics

\- Data Export Support



\---



\## 🛠️ Technologies Used



| Category | Technology |

|-----------|------------|

| Programming Language | Python |

| Web Scraping | Requests |

| HTML Parsing | BeautifulSoup |

| Automation | Selenium |

| Scraping Framework | Scrapy |

| Database | PostgreSQL |

| Dashboard | Streamlit |

| Data Processing | Pandas |

| Visualization | Plotly |

| Version Control | Git \& GitHub |



\---



\## 📂 Project Structure



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

│   ├── field\_detector.py

│   ├── parser.py

│   └── product\_parser.py

│

├── universal\_scraper/

│

├── universal\_v2.py

├── requirements.txt

├── run\_scraper.bat

├── README.md

└── .gitignore

```



\---



\# 📸 Project Screenshots



\## Dashboard Overview



!\[Dashboard Overview](screenshots/dashboard\_overview.png)



The Streamlit dashboard provides a centralized interface to explore and analyze scraped data.



\---



\## Search \& Filtering



!\[Dashboard Filters](screenshots/dashboard\_filters.png)



Users can filter products using:



\- Product Name

\- Minimum Price

\- Maximum Price

\- Stock Status



\---



\## Analytics Dashboard



!\[Dashboard Analytics](screenshots/dashboard\_analytics.png)



Interactive visualizations help understand:



\- Product distribution

\- Price trends

\- Inventory availability



\---



\## PostgreSQL Storage



!\[PostgreSQL Records](screenshots/postgresql\_records.png)



All extracted records are stored inside PostgreSQL for persistence and querying.



\---



\## Scraper Execution



!\[Scraper Execution](screenshots/scraper\_execution.png)



The scraper automatically processes web pages, extracts records, and stores them in the database.



\---



\## ⚙️ Installation



\### Clone Repository



```bash

git clone https://github.com/ayushsankhyan/Universal-Web-Scraper.git

cd Universal-Web-Scraper

```



\### Create Virtual Environment



```bash

python -m venv venv

```



\### Activate Environment



Windows:



```bash

venv\\Scripts\\activate

```



\### Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\## 🗄️ PostgreSQL Setup



Create Database:



```sql

CREATE DATABASE scraper\_db;

```



Update database credentials inside:



```text

scraper/db.py

dashboard/app.py

```



\---



\## ▶️ Running the Scraper



```bash

python universal\_v2.py

```



Example Input:



```text

https://books.toscrape.com

```



\---



\## 📊 Running the Dashboard



```bash

streamlit run dashboard/app.py

```



\---



\## 📈 Dashboard Capabilities



\- Search Products

\- Filter by Price

\- Filter by Stock Status

\- View Product Metrics

\- Analyze Price Distribution

\- Export Data

\- Explore Scraped Records



\---



\## 🎯 Learning Outcomes



Through this project I gained hands-on experience in:



\- Web Scraping

\- Data Extraction Techniques

\- BeautifulSoup

\- Selenium Automation

\- Scrapy Framework

\- PostgreSQL Database Management

\- Data Analytics

\- Dashboard Development

\- Git \& GitHub Workflow

\- End-to-End Data Pipeline Development



\---



\## 🔮 Future Enhancements



\- Multi-URL Scraping

\- Scheduled Scraping Jobs

\- AI-Based Field Detection

\- Cloud Deployment

\- REST API Integration

\- User Authentication

\- Real-Time Monitoring Dashboard



\---



\## 👨‍💻 Author



\### Ayush Sankhyan



BE CSE (Hons) – Artificial Intelligence \& Machine Learning  

Chandigarh University



GitHub: https://github.com/ayushsankhyan



\---



⭐ If you found this project interesting, consider giving it a star on GitHub.

