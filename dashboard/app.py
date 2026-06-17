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

st.markdown("""
Monitor and analyze scraped product data.

### How to use

**Search Title**
- Search for a product name

**Min Price**
- Minimum product price

**Max Price**
- Maximum product price

**Stock Filter**
- Filter products by stock availability
""")

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
# PRICE CLEANING
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
# KPIs
# -----------------------------
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
st.subheader(
    "📊 Price Distribution"
)

fig = px.histogram(
    df,
    x="Price",
    nbins=10,
    title="Product Price Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# TABLE
# -----------------------------
st.subheader(
    "📋 Products"
)

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# DOWNLOAD
# -----------------------------
csv = df.to_csv(
    index=False
)

st.download_button(
    "⬇ Download CSV",
    csv,
    "products.csv",
    "text/csv"
)