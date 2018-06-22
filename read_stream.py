from confluent_kafka import Consumer, KafkaError
import datetime
c = Consumer({'group.id': 'mygroup',
              'default.topic.config': {'auto.offset.reset': 'earliest'}})
c.subscribe(['/demo-stream:topic1'])
running = True
while running:
  msg = c.poll(timeout=1.0)
  if msg is None: continue
  if not msg.error():
    print('\n')
    print('*****Received message at: '+ str(datetime.datetime.fromtimestamp(msg.timestamp()[1] / 1e3)) + ' : ' +  msg.value().decode('utf-8'))
  elif msg.error().code() != KafkaError._PARTITION_EOF:
    print(msg.error())
    running = False
c.close()

