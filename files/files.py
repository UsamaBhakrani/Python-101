from pathlib import Path
import shutil
from zipfile import ZipFile
import csv

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

with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
