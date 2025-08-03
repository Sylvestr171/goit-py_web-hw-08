from typing import Any
from models import Authors, Quotes
from connect import connect, uri


def find_by_tag(*tag: str) -> list[str | None]:
    print(f"Find by {tag}")
    quotes_list = Quotes.objects(tags__in=tag)
    result = [q.quote for q in quotes_list]
    return result

def find_by_author(author: str) -> list[list[Any]]:
    print(f"Find by {author}")
    authors_list = Authors.objects(fullname=author)
    result = {}
    for item in authors_list:
        quotes_list = Quotes.objects(author=item)
        result[item.fullname] = [q.quote for q in quotes_list]
    return result


def main_cycle():
    while True:
        raw = input("Введи команду (команда: значення) або 'exit' для виходу: ").strip()

        if raw.upper() == "EXIT":
            print("End")
            break
        elif ":" not in raw:
            print("Невірний формат. Використовуй: команда: аргумент1,аргумент2")
            continue
        
        command_part, args_part = raw.split(":", 1)
        command = command_part.strip().lower()
        args = [arg.strip() for arg in args_part.split(",") if arg.strip()]

        if command == "name":
            result = find_by_author(args[0])
            print(result)
        elif command == "tag":
            result = find_by_tag(*args)
            print(result)

if __name__ == '__main__':
    main_cycle()

