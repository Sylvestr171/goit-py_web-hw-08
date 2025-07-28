from mongoengine import Document, ReferenceField
from mongoengine.fields import DateTimeField, StringField
from datetime import datetime

class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)
    created = DateTimeField(default=datetime.now(), required=True)

class Quotes (Document):
    tags = StringField(required=True)
    author = ReferenceField(Authors, required=True)
    quote = StringField(required=True)
    created = DateTimeField(default=datetime.now(), required=True)