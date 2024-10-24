from pathlib import Path
import shutil
from zipfile import ZipFile

# with ZipFile('files.zip', 'w') as zip:
#     for path in Path('ecommerce').rglob('*.*'):
#         zip.write(path)

with ZipFile('files.zip') as zip:
    print(zip.namelist())

    # Path('/user/local/bin/')
    # path = Path('ecommerce/__init__.py')
    # # paths = [p for p in path.iterdir()]
    # print(path.read_text())
    # shutil.copy()
