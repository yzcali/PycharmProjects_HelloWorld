from pathlib import Path

path = Path("ecommerce")
print(path.exists())  # True

# mkdir it means make a directory and rmdir it means remove directory
path = Path("emails")
# path.mkdir()
# path.rmdir()

# glob with this methods we can search for files and directories in the current path.
path = Path()
for file in path.glob('*.if.py'):  # use glob('*') for every files
    print(file)                    # app.12.if.py is found by glob('*.if.py')
