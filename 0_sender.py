import pika

# conncetion to my server
credentials = pika.PlainCredentials('mohammad','mohammad')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))


# make channel
# make q
ch = connection.channel()
# name for queue
ch.queue_declare(queue='one')

#send to queue
ch.basic_publish(exchange='',routing_key='one',body='hello word')

print('msg send it...')
connection.close()
