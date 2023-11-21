import pika

credeintals =  pika.PlainCredentials('mohammad','mohammad')
conntions =  pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credeintals))
ch = conntions.channel()
ch.queue_declare(queue='one')

def callback(ch,method,prop,body):
    print(f'received {body}')
ch.basic_consume('one',on_message_callback=callback,auto_ack=True)
ch.start_consuming()