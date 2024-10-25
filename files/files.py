import sqlite3
from pathlib import Path
import shutil
from zipfile import ZipFile
import csv
import json
# with ZipFile('files.zip', 'w') as zip:
#     for path in Path('ecommerce').rglob('*.*'):
#         zip.write(path)

# with ZipFile('files.zip') as zip:
#     print(zip.namelist())

# Path('/user/local/bin/')
# path = Path('ecommerce/__init__.py')
# # paths = [p for p in path.iterdir()]
# print(path.read_text())
# shutil.copy()

# CSV Files
# with open('data.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Age', 'City'])
#     writer.writerow(['John', 30, 'New York'])
#     writer.writerow(['Jane', 28, 'Los Angeles'])

# with open('data.csv') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# Working with JSON Objects

# movies = [
#     {"id": 1, "name": 'title 1', "age": '30'},
#     {"id": 2, "name": 'title 2', "age": '32'},
#     {"id": 3, "name": 'title 3', "age": '34'}
# ]

# data = json.dumps(movies)
# print(data)
# path = Path("movies.json").write_text(data)

# data = Path("movies.json").read_text()
# movies = json.loads(data)

# movies = json.loads(Path('movies.json').read_text())

# with sqlite3.connect('db.sqlite3') as conn:
#     command = 'INSERT INTO Movies VALUES(?,?,?)'
#     for movie in movies:
#         conn.execute(command, (movie['id'], movie['name'], movie['age']))
#     conn.commit()

# with sqlite3.connect('db.sqlite3') as conn:
#     command = 'SELECT * FROM Movies'
#     cursor = conn.execute(command)
#     for row in cursor:
#         print(row)

# import time
# print(time.time())


# def send_emails():
#     for i in range(10000):
#         pass


# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)

# from datetime import datetime, timedelta
# dt1 = datetime(2024, 10, 24) + timedelta(days=1)
# dt2 = datetime.now()
# duration = dt2 - dt1
# print(duration.seconds)
# dt = datetime.strptime('2018-01-30', '%Y-%m-%d')
# print(dt)

from random import random, randint, choice, choices
import string
print(random())
print(choice([1, 10, 5, 50]))
print(choices([1, 10, 5, 50], k=2))
print(randint(2, 3))
print("".join(choices(string.ascii_letters+string.digits, k=10)))
