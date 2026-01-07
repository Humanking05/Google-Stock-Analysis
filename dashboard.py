import streamlit as st
import pandas as pd
import sqlite3
import plotly.graph_objects as go
import streamlit_shadcn_ui as ui
import os

# Page Config
st.set_page_config(page_title="Google Stock Analysis", layout="wide")

# Title
st.title("Google Stock Analysis Dashboard")
st.markdown("Exploratory Data Analysis & Key Performance Indicators")

# Data Loading
@st.cache_data
def load_data():
    db_path = os.path.join("notebooks", "stock_data.db")
    if not os.path.exists(db_path):
        st.error(f"Database not found at {db_path}")
        return pd.DataFrame()
    
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM google_stock", conn)
    conn.close()
    
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

if df.empty:
    st.stop()

# Sidebar: Date Filter
st.sidebar.header("Filter Options")
min_date = df['date'].min().date()
max_date = df['date'].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

if len(date_range) == 2:
    start_date, end_date = date_range
    # Filter Data
    filtered_df = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]
else:
    # If range selection is incomplete (only one date picked), show all or wait
    start_date, end_date = min_date, max_date
    filtered_df = df

# KPI Calculations
avg_close = filtered_df['close'].mean()
price_volatility = filtered_df['close'].std()
avg_daily_range = (filtered_df['high'] - filtered_df['low']).mean()
avg_volume = filtered_df['volume'].mean()

# Trend Calculations
upward_trend_days = (filtered_df['close'] > filtered_df['close'].shift(1)).sum()
downward_trend_days = (filtered_df['close'] < filtered_df['close'].shift(1)).sum()
high_vol_spikes = (filtered_df['volume'] > (filtered_df['volume'].mean() * 2)).sum()
gap_days = ((abs(filtered_df['open'] - filtered_df['close'].shift(1)) / filtered_df['close'].shift(1)) > 0.01).sum()

st.subheader("Key Performance Indicators")

# Row 1: Price & Volatility
cols = st.columns(4)
with cols[0]:
    ui.metric_card(title="Avg Close Price", content=f"${avg_close:.2f}", description="Average closing price over selected period")
with cols[1]:
    ui.metric_card(title="Price Volatility", content=f"{price_volatility:.2f}", description="Standard deviation of closing price")
with cols[2]:
    ui.metric_card(title="Avg Daily Range", content=f"${avg_daily_range:.2f}", description="Average high-low difference")
with cols[3]:
    ui.metric_card(title="Avg Volume", content=f"{avg_volume:,.0f}", description="Average daily trading volume")

# Row 2: Trends & Anomalies
cols2 = st.columns(4)
with cols2[0]:
    ui.metric_card(title="Upward Trend Days", content=f"{upward_trend_days}", description="Days where close > prev close")
with cols2[1]:
    ui.metric_card(title="Downward Trend Days", content=f"{downward_trend_days}", description="Days where close < prev close")
with cols2[2]:
    ui.metric_card(title="High Vol Spikes", content=f"{high_vol_spikes}", description="Days with volume > 2x average")
with cols2[3]:
    ui.metric_card(title="Gap Days", content=f"{gap_days}", description="Days with >1% open gap")

# Charts
st.subheader("Price & Volume Analysis")

# Price Chart
fig_price = go.Figure()
fig_price.add_trace(go.Scatter(x=filtered_df['date'], y=filtered_df['close'], mode='lines', name='Close Price'))
fig_price.update_layout(title="Stock Closing Price Over Time", xaxis_title="Date", yaxis_title="Price ($)")
st.plotly_chart(fig_price, use_container_width=True)

# Volume Chart
fig_vol = go.Figure()
fig_vol.add_trace(go.Bar(x=filtered_df['date'], y=filtered_df['volume'], name='Volume', marker_color='orange'))
fig_vol.update_layout(title="Trading Volume Over Time", xaxis_title="Date", yaxis_title="Volume")
st.plotly_chart(fig_vol, use_container_width=True)

# Raw Data (Optional)
with st.expander("View Raw Data"):
    st.dataframe(filtered_df)
