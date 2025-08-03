import pika
from models import Contacts
from seeds import insert_contacts_to_mongo
import json


insert_contacts_to_mongo(10, 15)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='send_email')

contact_list = Contacts.objects()
contact_dict = {contact.id : [contact.fullname, contact.email, contact.Checkbox] for contact in contact_list}

for key in contact_dict:
    data = contact_dict.get(key)
    json_str = json.dumps(data, ensure_ascii=False)
    message_byte = json_str.encode('utf-8')

    channel.basic_publish(exchange='', routing_key='send_email', body=message_byte)

    print(f" [x] Sent '{data}'")
connection.close()
