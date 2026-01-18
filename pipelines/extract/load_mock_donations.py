import pandas as pd

def extract_data():
    return pd.read_csv('/opt/airflow/data/mock_donations.csv')
