import pandas as pd
from datetime import datetime

def build_features(clean_dict):
    df = pd.DataFrame(clean_dict)
    snapshot_date = datetime(2024, 12, 31)

    agg = df.groupby('donor_id').agg(
        total_donations=('donation_amount', 'sum'),
        donation_count=('donation_amount', 'count'),
        last_donation=('donation_date', 'max'),
        avg_donation=('donation_amount', 'mean')
    ).reset_index()

    agg['days_since_last'] = (snapshot_date - agg['last_donation']).dt.days

    return agg[['donor_id', 'total_donations', 'donation_count', 'avg_donation', 'days_since_last']]
