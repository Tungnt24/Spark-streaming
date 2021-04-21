import os
from dotenv import load_dotenv

load_dotenv()

class KafkaConfig():
	KAFKA_BROKER = os.getenv("KAFKA_BROKER")
	KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")