from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import json
import requests
from kafka import KafkaProducer
import time
import logging

default_args = {
    'owner': 'andreia',
    'start_date': datetime(2023, 11, 10, 18, 00)
}

def get_data():
    # connecting with the API
    response = requests.get('https://randomuser.me/api/').json()
    # Retrieving just the result with the information part
    response = response['results'][0]
    
    return response

def clean_data(response):
    data = {}
    location = response['location']
    # Preparation of the data for streaming with kafka
    data['id'] = response['login']['uuid']
    data['gender'] = response['gender']
    data['first_name'] = response['name']['first']
    data['last_name'] = response['name']['last']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['email'] = response['email']
    data['username'] = response['login']['username']
    data['dob_date'] = response['dob']['date']
    data['register_date'] = response['registered']['date']
    data['phone'] = response['phone']
    data['picture'] = response['picture']['medium']
    
    return data

def stream_kafka():
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    time_now = time.time()
    
    # Streaming data during 1 minute to get multiple profiles from the API
    # If it's done once, only one profile will be acquired
    while True:
        if time_now > time_now + 60:
            break
        try:
            response = get_data()
            cleaning = clean_data(response)  
            print(json.dumps(cleaning, indent=3))
            producer.send('users_created', json.dumps(cleaning).encode('utf-8'))
        except Exception as error:
            logging.error(f'Error: {error}')
            continue

with DAG('user_automation',
         default_args=default_args,
         schedule='@daily',
         catchup=False) as dag:
    
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_kafka
    )
