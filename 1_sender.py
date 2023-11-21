import pika
import time
credeitals =  pika.PlainCredentials('mohammad','mohammad')
connctions = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credeitals))


ch =  connctions.channel()
ch.queue_declare(queue='one')
ch.basic_publish(exchange='',routing_key='one',body='hello word 1',properties=pika.BasicProperties(content_type='test/plain',content_encoding='zgip',user_id='10',delivery_mode=2,))
print('msg send it...')
connctions.close()