from kafka import KafkaProducer
import json,time
from data_generator import get_registered_user

def json_converter(data):
    return json.dumps(data).encode("utf-8")


    """partitioner method with 3 parameters
    key_bytes
    all_partition
    avaliable_partition
    """
# def get_partition(key, all, avaliable):
#     return 0

producer = KafkaProducer( bootstrap_servers = ['localhost:9092'],
                         value_serializer= json_converter,)
                        #  partitioner = get_partition)
                        
if __name__=="__main__":
    while True:
        user = get_registered_user()
        print(user)
        producer.send('cha19',user)
        time.sleep(5)