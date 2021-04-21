import os
import json
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from src.configuration.spark_window_config import WindowConfig
from src.configuration.kafka_config import KafkaConfig


def echo(time, rdd):
    counts = f"Event {time} {rdd.collect()}"
    print(counts)
    print(f"Appending to {os.path.abspath('events_log')}")
    with open("events_log.txt", "a") as f:
        data = {f"{time}": {event[0]: event[1:] for event in rdd.collect()}}
        json.dump(data, f)
        f.write("\n\n")


def set_event(data):
    return (data[data.rfind(",") + 1 :], data)


def aggregate_by_key(a, b):
    return f"{a}, {b}"


def create_context(broker, topic):
    sc = SparkContext(appName="Python Streaming")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 1)
    kvs = KafkaUtils.createDirectStream(
        ssc, [topic], {"metadata.broker.list": broker}
    )
    lines = kvs.map(lambda event: event[1])
    words = lines.window(
        windowDuration=WindowConfig.WINDOW_DURATION,
        slideDuration=WindowConfig.SLIDE_DURATION).map(set_event).reduceByKey(aggregate_by_key)
    words.foreachRDD(echo)
    return ssc


if __name__ == "__main__":
    broker, topic = sys.argv[1:]
    ssc = StreamingContext.getOrCreate(
        "checkpoint",
        lambda: create_context(
            KafkaConfig.KAFKA_BROKER, KafkaConfig.KAFKA_TOPIC
        ),
    )
    ssc.start()
    ssc.awaitTermination()
