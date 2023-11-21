import pika
credentials = pika.PlainCredentials('mohammad','mohammad')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))

ch = connection.channel()

ch.queue_declare(queue='one')



def callback(ch,method,properites,body):
    print(f"Received {body}")
    

ch.basic_consume(queue='one',on_message_callback=callback,auto_ack=True)
print("waitin for message to exit ctrl+c")
ch.start_consuming()




