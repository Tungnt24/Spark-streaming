# Spark-streaming
Spark streaming with kafka 


# Run

```python3 src/app.py <kafka_bootstrap_server> <kafka_topic>```

# Re-process

- add event to ```reprocess_event.txt```
- run ```python3 src/kafka_producer.py <kafka_bootstrap_server> <kafka_topic>```


## Send event with kafka-python

open your ```ipython```

```python
  from kafka import KafkaProducer
  producer = KafkaProducer(bootstrap_servers=<kafka_bootstrap_server>)
  event = "example1,example2,example3"
  producer.send(topic, bytes(event, "utf-8"))
```
