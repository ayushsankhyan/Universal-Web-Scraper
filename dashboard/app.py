import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px


# -----------------------------
# DATABASE
# -----------------------------
def get_products():

    connection = psycopg2.connect(
        host="localhost",
        database="scraper_db",
        user="postgres",
        password="12345"
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            url,
            title,
            price,
            stock
        FROM scraped_products
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows


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
Monitor, search and analyze data scraped from websites.

### How to use

**Search Title**
- Type part of a product name
- Example: `sharp`

**Min Price**
- Show products above a certain price
- Example: `20`

**Max Price**
- Show products below a certain price
- Example: `50`

**Stock Filter**
- Show only products matching stock status
""")

# -----------------------------
# LOAD DATA
# -----------------------------
rows = get_products()

if not rows:
    st.warning("No products found.")
    st.stop()

df = pd.DataFrame(
    rows,
    columns=[
        "ID",
        "URL",
        "Title",
        "Price",
        "Stock"
    ]
)

# -----------------------------
# CLEAN PRICE COLUMN
# -----------------------------
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🔍 Filters")

search = st.sidebar.text_input(
    "Search Title",
    help="Example: sharp, sapiens, velvet"
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
    [
        "All",
        "In stock"
    ]
)

# -----------------------------
# FILTERING
# -----------------------------
if search:

    df = df[
        df["Title"]
        .astype(str)
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
col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📚 Products",
        len(df)
    )

with col2:

    avg_price = round(
        df["Price"].mean(),
        2
    )

    st.metric(
        "💷 Average Price",
        avg_price
    )

with col3:

    st.metric(
        "✅ In Stock",
        len(
            df[
                df["Stock"] == "In stock"
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
# DOWNLOADS
# -----------------------------
st.subheader(
    "⬇ Export Data"
)

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
# URL SUMMARY
# -----------------------------
st.subheader(
    "🌍 Sources"
)

source_counts = (
    df["URL"]
    .value_counts()
    .reset_index()
)

source_counts.columns = [
    "URL",
    "Records"
]

st.dataframe(
    source_counts,
    use_container_width=True
)