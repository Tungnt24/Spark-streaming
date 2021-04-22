# Spark-streaming
Spark streaming with kafka 

# Usage

create virtualenv: ```virtualenv venv --python=python3.7```

```pip install -r requirements.txt```

create file ```.env```  
and add your config 

detail in ```.env.example```

# Run

```python3 src/app.py```

# Re-process

- copy events from ```events_log.txt``` to ```reprocess_event.txt```
- run ```python3 src/kafka_producer.py```


## Send event with kafka-python

open your ```ipython```

```python
  from kafka import KafkaProducer
  producer = KafkaProducer(bootstrap_servers=<kafka_bootstrap_server>)
  event = "example1,example2,example3"
  producer.send(topic, bytes(event, "utf-8"))
```
