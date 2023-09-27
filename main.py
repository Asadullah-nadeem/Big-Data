import pymysql
import json
from datetime import datetime
import random

# Connect to MySQL
conn = pymysql.connect(host='localhost', user='root', password='',port=3308, database='bigdata')
cursor = conn.cursor()

# Sample data generation
def generate_sample_data():
    payload = {
        'temperature': random.uniform(20.0, 40.0),
        'humidity': random.uniform(40.0, 80.0)
    }
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return payload, created_at

# Insert sample data into MySQL
for _ in range(1000):
    payload, created_at = generate_sample_data()
    cursor.execute("INSERT INTO data (payload, created_at) VALUES (%s, %s)", (json.dumps(payload), created_at))

# Commit the changes and close connection
conn.commit()
conn.close()
