# Donor Intelligence Platform (Apache Airflow)

End-to-end data engineering portfolio project for predicting which donors are most likely to donate again.

## Descripton:
This project simulates a real nonprofit use case. I built an Airflow pipeline that ingests donation data, performs feature engineering using RFM metrics, runs data quality checks using Great Expectations, scores donors by likelihood to donate again, and publishes analytics-ready tables. I also built a Streamlit dashboard for stakeholders

## Features
- Apache Airflow orchestration
- Feature engineering (RFM metrics)
- Donor scoring model
- Great Expectations data quality checks
- Postgres warehouse
- Streamlit dashboard
- Dockerized setup
- Tests
- Demo script for interviews

## Run
docker-compose up --build

Airflow UI: http://localhost:8080 (airflow / airflow)

## Demo
python demo_script.py
