import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "cha19",
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='consumergroup_a'
)

print("starting consumer")

for msg in consumer:
    print("users = {} ".format(json.loads(msg.value)))