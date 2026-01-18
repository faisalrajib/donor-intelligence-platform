import pandas as pd

def clean_data(raw_dict):
    df = pd.DataFrame(raw_dict)
    df['donation_date'] = pd.to_datetime(df['donation_date'])
    df = df.dropna(subset=['donor_id', 'donation_amount'])
    return df
