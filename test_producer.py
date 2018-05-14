from confluent_kafka import Producer
p = Producer({'streams.producer.default.stream': '/demo-stream'})
some_data_source=["msg1","msg2","msg3"]
for data in some_data_source:
  p.produce('topic1', data.encode('utf-8'))
  p.flush()
