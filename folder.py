import os

folders = [
    "app/api", "app/core", "app/services",
    "app/models", "app/utils"
]
files = ["main.py"]

for f in folders:
    os.makedirs(f, exist_ok=True)

for file in files:
    open(file, 'w').close()