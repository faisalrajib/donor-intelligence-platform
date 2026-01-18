import streamlit as st
import psycopg2
import pandas as pd

st.title("Donor Intelligence Dashboard")

conn = psycopg2.connect(
    host="localhost",
    dbname="airflow",
    user="airflow",
    password="airflow",
    port=5432
)

query = "SELECT * FROM donor_scores ORDER BY donor_score DESC"
df = pd.read_sql(query, conn)
conn.close()

st.dataframe(df)
st.bar_chart(df.set_index("donor_id")["donor_score"])
