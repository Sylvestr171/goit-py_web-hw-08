#json loader
from models import Authors, Quotes
import json


with open("authors.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    for item in data:
        if not Authors.objects(fullname=item["fullname"]).first():
            try:
                author = Authors(**item)
                author.save()
            except Exception as e:
                print(f"Помилка: {e}")


with open("qoutes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    for item in data:
        if not Quotes.objects(tags=item["tags"]).first():
            try:
                author = Quotes(**item)
                author.save()
            except Exception as e:
                print(f"Помилка: {e}")

