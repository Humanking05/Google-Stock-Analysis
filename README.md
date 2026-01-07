# 📈 Google Stock KPI Analysis

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite\&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit\&logoColor=white)

---

## 📌 Project Overview

This project delivers a **business-focused stock performance analysis** using historical Google (GOOG) market data. The goal is to translate raw price and volume data into **clear, decision-ready KPIs** that support executive, investment, and trading decisions.

All KPIs are calculated **directly in SQLite**, ensuring transparency, reproducibility, and database-first analytics. Python is used strictly as an execution layer, while insights are embedded at the query level for immediate interpretation.

---

## 🗂️ Dataset

The dataset contains historical stock market data with the following columns:

* `symbol`
* `date`
* `open`
* `high`
* `low`
* `close`
* `volume`

---

## 🧠 Business Problem

Investors and portfolio managers need to understand:

* How a stock behaves over time
* The level of risk and volatility involved
* Liquidity and trading activity strength
* Whether the stock supports long-term investment, short-term trading, or both

This project answers these questions using **clearly defined KPIs with business insights**.

---

## 📊 Key Performance Indicators (KPIs)

Each KPI is calculated **independently** using SQLite and returns:

* The KPI value
* A plain-English business insight

### Metric KPIs

* Average Closing Price
* Price Volatility
* Average Daily Range
* Average Trading Volume

### Non-Metric KPIs

* Upward Trend Days
* Downward Trend Days
* High-Volume Spike Days
* Price Gap Days

---

## 📁 Project Structure

```
project-root/
│
├── notebook_1_google_stock_analysis Plan.ipynb  
├── notebook_2_data_loading_and_cleaning.ipynb 
├── notebook_3_exploratory_data_analysis.ipynb
├── notebook_4_google_stock_performance_analysis.ipynb
├── notebook_5_portfolio_allocation_guidance.ipynb
├── notebook_6_c-suite_board_level_summary.ipynb                  
├── stock_data.db                  
├── dashboard.py                      
└── requirements.txt
```

---

## 🧪 Tools & Technologies

* **Python** – Query execution and orchestration
* **SQLite** – KPI computation and data storage
* **Jupyter Notebook** – Step-by-step analysis and documentation
* **Streamlit** – Optional interactive business dashboard

---

## 📈 Business Outcomes

* Clear visibility into **price behavior, risk, and liquidity**
* Actionable insights for **Buy / Hold / Trade decisions**
* Executive-ready summaries for **portfolio allocation discussions**
* A scalable framework reusable for **any equity or financial dataset**

---

## 🧾 Executive Insight (GOOG)

GOOG demonstrates strong liquidity, consistent trading activity, and a long-term upward bias, balanced by elevated volatility. The stock supports both long-term growth strategies and tactical trading approaches when managed with disciplined risk controls.

---

## 🚀 How to Run

1. Clone the repository
2. Open notebooks in Jupyter
3. Ensure `stock_data.db` is in the project root
4. Run KPI queries individually in **Notebook 3**
5. (Optional) Launch Streamlit app:

```bash
streamlit run app.py
```

---

## 📎 Use Cases

* Investment research
* Portfolio strategy reviews
* Executive reporting
* Financial analytics portfolios

---

## 🏁 Final Note

This project emphasizes **clarity, separation of logic, and business relevance**—turning raw market data into insights that decision-makers can act on with confidence.

👤 Author

Hassan Rafindadi Data Analyst | Business Intelligence | Python | SQL | BI Tools

📧 Email: rafindadihassan@gmail.com 🔗 LinkedIn: https://www.linkedin.com/in/hassan-rafindadi-8704a41b4

Dashboard link: https://app-stock-analysis-hebrrtmb3a4hjmv5a2vpjt.streamlit.app/
