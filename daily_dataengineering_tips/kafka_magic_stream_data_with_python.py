from kafka import KafkaProducer, KafkaConsumer

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send a message to the 'clickstream' topic
producer.send('clickstream', b'user123 clicked on the homepage')
producer.flush()

# Create a Kafka consumer
consumer = KafkaConsumer(
    'clickstream',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest', # Start at the beginning of the topic
    group_id='clickstream_group'
)

# Consume messages
for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
