from mongoengine import Document, BooleanField
from mongoengine.fields import DateTimeField, StringField, ListField
from datetime import datetime
from connect import connect

class Contacts(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    Checkbox = BooleanField(required=True)
    created = DateTimeField(default=datetime.now(), required=True)