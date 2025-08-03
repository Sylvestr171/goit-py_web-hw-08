import os
import sys
from time import sleep
import pika
from bson import ObjectId
from models import Contacts

def send_email(data):
    sleep(1)
    return data[2:26]

def update_checkbox_to_true(id_for_change):
    try:
        obj_id = ObjectId(id_for_change)
        document = Contacts.objects(id=obj_id).first()
        if document:
            document.Checkbox = True
            document.save()
            print("✅ MongoDB: checkbox оновлено на True")
        else:
            print("⚠️ Користувача з таким id не знайдено")
    except Exception as e:
        print(f"❌ Помилка оновлення: {e}")


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='send_email')

    def callback(ch, method, properties, body):
        data=body.decode()
        print(f" [x] Received {data}")
        id = send_email(data)
        print (f">>>>>>{id}")
        update_checkbox_to_true(id)

    channel.basic_consume(queue='send_email', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
