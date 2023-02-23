# Searches a SQLite3 database using first name, last name, or birth date

Start by importing the necessary libraries:

```python
import sqlite3
```

Connect to the SQLite3 database:

```python
conn = sqlite3.connect('user_database.db')
```

Create a cursor object to execute SQL commands:

```python
cursor = conn.cursor()
```

Create a table to store user information:

```python
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    birth_date TEXT,
    valid INTEGER
)
''')
```

Insert some data into the table:

```python
cursor.execute("INSERT INTO users (first_name, last_name, birth_date) VALUES ('John', 'Doe', '1990-01-01',1)")
cursor.execute("INSERT INTO users (first_name, last_name, birth_date) VALUES ('Jane', 'Doe', '1995-05-05',0)")
```

Commit the changes to the database:

```python
conn.commit()
```

Define a function to search for users based on first name, last name, or birth date:

```python
def search_user(first_name=None, last_name=None, birth_date=None):
    query = "SELECT * FROM users WHERE 1=1"
    if first_name:
        query += f" AND first_name = '{first_name}'"
    if last_name:
        query += f" AND last_name = '{last_name}'"
    if birth_date:
        query += f" AND birth_date = '{birth_date}'"
    cursor.execute(query)
    return cursor.fetchall()
```

Call the search_user function with different parameters to search for users in the database:

```python
print(search_user(first_name='John'))
print(search_user(last_name='Doe'))
print(search_user(birth_date='1995-05-05'))
```

This is just a basic example of how you could create a Python app that searches a SQLite3 database using first name, last name, or birth date. You could also add additional functionality, such as the ability to add new users or update existing users, if needed.