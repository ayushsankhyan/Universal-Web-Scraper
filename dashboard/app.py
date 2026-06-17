
import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Universal Scraper Dashboard",
    page_icon="🌐",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🌐 Universal Scraper Dashboard")

st.info("""
📚 **Current Dataset Source:** Books To Scrape

🔗 Website: https://books.toscrape.com

This dashboard visualizes product data collected using a custom-built web scraping pipeline.
""")

# -----------------------------
# PROJECT METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🌍 Source",
        "BooksToScrape"
    )

with col2:
    st.metric(
        "📦 Dataset",
        "1000 Records"
    )

with col3:
    st.metric(
        "🛠️ Stack",
        "Python"
    )

# -----------------------------
# PROJECT INFO
# -----------------------------
st.subheader("📌 Project Overview")

st.markdown("""
### 🌍 Source Website

[🔗 Visit Books To Scrape](https://books.toscrape.com)

### Purpose

This project demonstrates a complete web scraping and analytics workflow.

### Technologies Used

- Python
- Requests
- BeautifulSoup
- Selenium
- Scrapy
- PostgreSQL
- Pandas
- Streamlit
- Plotly

### Extracted Fields

- Product Title
- Product Price
- Stock Availability

### Workflow

Website → Scraper → Data Cleaning → Storage → Dashboard Analytics
""")

st.markdown("---")

# -----------------------------
# LOAD DATA
# -----------------------------
try:

    df = pd.read_csv("data/products.csv")

except Exception as e:

    st.error(f"Error loading CSV: {e}")
    st.stop()

# -----------------------------
# FIX COLUMN NAMES
# -----------------------------
df.columns = [
    col.strip().title()
    for col in df.columns
]

# -----------------------------
# CLEAN PRICE
# -----------------------------
df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🔍 Filters")

search = st.sidebar.text_input(
    "Search Title"
)

min_price = st.sidebar.number_input(
    "Min Price",
    value=0.0
)

max_price = st.sidebar.number_input(
    "Max Price",
    value=float(df["Price"].max())
)

stock_filter = st.sidebar.selectbox(
    "Stock Status",
    ["All"] + sorted(df["Stock"].unique())
)

# -----------------------------
# FILTERING
# -----------------------------
if search:

    df = df[
        df["Title"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

df = df[
    (df["Price"] >= min_price)
    &
    (df["Price"] <= max_price)
]

if stock_filter != "All":

    df = df[
        df["Stock"] == stock_filter
    ]

# -----------------------------
# KPI CARDS
# -----------------------------
st.subheader("📈 Analytics Overview")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📚 Products",
        len(df)
    )

with col2:

    st.metric(
        "💷 Average Price",
        round(df["Price"].mean(), 2)
    )

with col3:

    st.metric(
        "✅ In Stock",
        len(
            df[
                df["Stock"]
                .str.contains(
                    "In stock",
                    na=False
                )
            ]
        )
    )

# -----------------------------
# CHART
# -----------------------------
st.subheader("📊 Price Distribution")

fig = px.histogram(
    df,
    x="Price",
    nbins=15,
    title="Product Price Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# TABLE
# -----------------------------
st.subheader("📋 Product Records")

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# DOWNLOAD
# -----------------------------
st.subheader("⬇ Export Data")

csv = df.to_csv(
    index=False
)

st.download_button(
    "Download CSV",
    csv,
    "products.csv",
    "text/csv"
)

# -----------------------------
# DATA SUMMARY
# -----------------------------
st.subheader("📊 Dataset Summary")

summary = pd.DataFrame({
    "Metric": [
        "Total Products",
        "Average Price",
        "Minimum Price",
        "Maximum Price"
    ],
    "Value": [
        len(df),
        round(df["Price"].mean(), 2),
        round(df["Price"].min(), 2),
        round(df["Price"].max(), 2)
    ]
})

st.dataframe(
    summary,
    use_container_width=True
)

