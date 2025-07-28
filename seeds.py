#json loader
from models import Authors, Quotes
import json


with open("authors.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for ithem in data:
    if not Authors.objects(fullname=ithem["fullname"]).first():
        author = Authors(**ithem)
        author.save()

with open("authors.json", "r", encoding="utf-8") as f:
    data = json.load(f)