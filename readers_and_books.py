import json
from csv import DictReader

with open("./data/users.json", mode="r") as j:
    users = json.load(j)

with open('./data/books.csv', newline='') as c:
    books = iter(list(DictReader(c)))

readers_and_books = list()

for user in users:
    reader = dict()
    reader["name"] = user["name"]
    reader["gender"] = user["gender"]
    reader["address"] = user["address"]

    try:
        reader["books"] = [next(books)]
    except StopIteration:
        reader["books"] = list()

    readers_and_books.append(reader)

print(readers_and_books)