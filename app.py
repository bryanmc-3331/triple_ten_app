import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Car Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()

# Header
st.header("🚗 Car Sales Dashboard")
st.write(
    "This app shows basic patterns in a car sales dataset. "
    "Use the filters in the sidebar to explore!"
)

# Sidebar filters
st.sidebar.subheader("Filters")
price_min = int(df["price"].min())
price_max = int(df["price"].max())
price_range = st.sidebar.slider("Price range ($)", price_min, price_max, (price_min, price_max))

filtered = df[(df["price"] >= price_range[0]) & (df["price"] <= price_range[1])].copy()

show_trend = st.checkbox("Show trendline on scatter plot")

# Histogram
st.subheader("Price Distribution")
hist = px.histogram(filtered, x="price", nbins=50, title="Price Histogram")
st.plotly_chart(hist, use_container_width=True)

# Scatter plot
st.subheader("Odometer vs. Price")
scatter = px.scatter(filtered, x="odometer", y="price", title="Odometer vs. Price", opacity=0.6)
if show_trend:
    scatter = px.scatter(filtered, x="odometer", y="price", trendline="ols",
                         title="Odometer vs. Price (with Trendline)", opacity=0.6)
st.plotly_chart(scatter, use_container_width=True)

st.caption("Data: vehicles_us.csv · Built with Streamlit, Pandas, and Plotly")
