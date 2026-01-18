"""
Interview Demo Script
---------------------
Run this while sharing your screen in interviews.

It explains the project while showing real output.
"""

from pipelines.extract.load_mock_donations import extract_data
from pipelines.transform.clean_donations import clean_data
from pipelines.transform.build_features import build_features
from pipelines.model.donor_scoring import score_donors

print("\nSTEP 1: Extracting data")
raw = extract_data()
print(raw.head())

print("\nSTEP 2: Cleaning data")
clean = clean_data(raw.to_dict())
print(clean.head())

print("\nSTEP 3: Feature engineering")
features = build_features(clean.to_dict())
print(features)

print("\nSTEP 4: Donor scoring")
scored = score_donors(features.to_dict())
print(scored.sort_values(by='donor_score', ascending=False))

print("\nDemo complete. This is the same logic orchestrated by Airflow.")
