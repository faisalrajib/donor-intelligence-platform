import psycopg2
import pandas as pd

def load_data(scored_dict):
    df = pd.DataFrame(scored_dict)

    conn = psycopg2.connect(
        host="postgres",
        dbname="airflow",
        user="airflow",
        password="airflow"
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS donor_scores (
            donor_id INT,
            total_donations FLOAT,
            donation_count INT,
            days_since_last INT,
            donor_score FLOAT
        )
    """)

    cur.execute("DELETE FROM donor_scores")

    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO donor_scores VALUES (%s, %s, %s, %s, %s)",
            tuple(row)
        )

    conn.commit()
    cur.close()
    conn.close()
