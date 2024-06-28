import pymongo
from pymongo import MongoClient
import random
from datetime import datetime, timedelta

# Conectar a MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client.parkingData
collection = db.parkings

# Generar datos simulados
def generate_simulated_data(num_records):
    levels = ['1', '2', '3', '4']
    slots = [f'A{i}' for i in range(1, 11)]
    data = []

    for _ in range(num_records):
        level_id = random.choice(levels)
        slot_id = random.choice(slots)
        entry_time = datetime.now() - timedelta(days=random.randint(0, 10), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        exit_time = entry_time + timedelta(hours=random.randint(1, 5))

        record = {
            'levelId': level_id,
            'slotId': slot_id,
            'entryTime': entry_time,
            'exitTime': exit_time
        }
        data.append(record)

    return data

# Insertar datos en MongoDB
def insert_data(data):
    try:
        collection.insert_many(data)
        print(f'{len(data)} records inserted successfully')
    except Exception as e:
        print(f'Error inserting data: {e}')

# Generar e insertar 100 registros simulados
simulated_data = generate_simulated_data(100)
insert_data(simulated_data)
