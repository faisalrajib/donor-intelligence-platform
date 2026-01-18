import pandas as pd

def score_donors(features_dict):
    df = pd.DataFrame(features_dict)

    df['freq_norm'] = df['donation_count'] / df['donation_count'].max()
    df['amt_norm'] = df['avg_donation'] / df['avg_donation'].max()
    df['recency_norm'] = 1 - (df['days_since_last'] / df['days_since_last'].max())

    df['donor_score'] = (
        0.4 * df['freq_norm'] +
        0.4 * df['recency_norm'] +
        0.2 * df['amt_norm']
    )

    return df[['donor_id', 'total_donations', 'donation_count', 'days_since_last', 'donor_score']]
