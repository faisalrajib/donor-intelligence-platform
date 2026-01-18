from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from pipelines.extract.load_mock_donations import extract_data
from pipelines.transform.clean_donations import clean_data
from pipelines.transform.build_features import build_features
from pipelines.model.donor_scoring import score_donors
from pipelines.quality.validate_with_ge import validate_data
from pipelines.load.load_to_postgres import load_data

def extract_task(**context):
    df = extract_data()
    context['ti'].xcom_push(key='raw', value=df.to_dict())

def clean_task(**context):
    raw = context['ti'].xcom_pull(key='raw')
    df = clean_data(raw)
    context['ti'].xcom_push(key='clean', value=df.to_dict())

def feature_task(**context):
    clean = context['ti'].xcom_pull(key='clean')
    df = build_features(clean)
    context['ti'].xcom_push(key='features', value=df.to_dict())

def scoring_task(**context):
    features = context['ti'].xcom_pull(key='features')
    df = score_donors(features)
    context['ti'].xcom_push(key='scored', value=df.to_dict())

def validate_task(**context):
    scored = context['ti'].xcom_pull(key='scored')
    df = validate_data(scored)
    context['ti'].xcom_push(key='validated', value=df.to_dict())

def load_task(**context):
    validated = context['ti'].xcom_pull(key='validated')
    load_data(validated)

with DAG(
    dag_id='donor_scoring_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@weekly',
    catchup=False,
) as dag:

    extract = PythonOperator(task_id='extract', python_callable=extract_task)
    clean = PythonOperator(task_id='clean', python_callable=clean_task)
    features = PythonOperator(task_id='features', python_callable=feature_task)
    score = PythonOperator(task_id='score', python_callable=scoring_task)
    validate = PythonOperator(task_id='validate', python_callable=validate_task)
    load = PythonOperator(task_id='load', python_callable=load_task)

    extract >> clean >> features >> score >> validate >> load
