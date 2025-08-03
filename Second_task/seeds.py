from models import Contacts
from random import randint
from faker import Faker
from models import Contacts

fake = Faker('uk-Ua')

class Contact():
    def __init__(self):
        self.name = fake.name()
        self.email = fake.email()
        self.checkbox = False

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, SendEmail: {self.checkbox}"

def insert_contacts_to_mongo(min_contact_namber, max_contact_number):
    for i in range(randint(min_contact_namber, max_contact_number)):
        contact = Contact()
        try:
            contact_for_mongo = Contacts(fullname=contact.name, email=contact.email, Checkbox=contact.checkbox)
            contact_for_mongo.save()
        except Exception as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    insert_contacts_to_mongo(10, 15)



