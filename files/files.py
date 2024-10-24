from pathlib import Path
import shutil
Path('/user/local/bin/')
path = Path('ecommerce/__init__.py')
# paths = [p for p in path.iterdir()]
print(path.read_text())
shutil.copy()
