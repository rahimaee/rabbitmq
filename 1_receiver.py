import pika
import time
credeintals =  pika.PlainCredentials('mohammad','mohammad')
conntions =  pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credeintals))
ch = conntions.channel()
ch.queue_declare(queue='one')

ch.basic_qos(prefetch_count=1)

def callback(ch,method,properties,body):
    print(f'received {body}')
    print(f'prop {properties}')
    print(method)
    time.sleep(3)
    print("done")
    ch.basic_ack(delivery_tag=method.delivery_tag)



ch.basic_consume('one',on_message_callback=callback)

ch.start_consuming()