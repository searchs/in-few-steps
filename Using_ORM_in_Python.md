# Using ORM in Python

An Object Relational Mapper (ORM) is a tool used in Python to interact with databases. It provides a convenient way to map between the database and the code, allowing you to perform database operations without writing raw SQL queries.

In this tutorial, we will be using the popular SQLAlchemy ORM to demonstrate how to interact with a database using an ORM in Python.

Step 1: Installing SQLAlchemy

You can install SQLAlchemy using pip by running the following command in your terminal:


```python
pip install sqlalchemy
```



To connect to a database using SQLAlchemy, you need to create an instance of the sqlalchemy.engine.Engine class. You can do this by providing the connection string to your database:

```python
from sqlalchemy import create_engine

# SQLite database
engine = create_engine('sqlite:///db.sqlite')

# PostgreSQL database
engine = create_engine('postgresql://username:password@localhost/dbname')

# MariaDB
engine = create_engine('mariadb://username:password@host:port/database')


```

Step 3: Defining Models

In SQLAlchemy, you define your database tables as classes. These classes are called models. To create a model, you need to import the sqlalchemy.ext.declarative.declarative_base class and create a subclass of it:

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

```

In the example above, we created a model called User with three fields: id, name, and age. The id field is defined as the primary key for the table.

Step 4: Creating the Table

To create the table for the model, you need to call the create_all method on the Base object and pass in the engine as an argument:

```python
Base.metadata.create_all(engine)
```


Step 5: Creating a Session

A session in SQLAlchemy is a unit of work with the database. You can use a session to perform database operations, such as adding, updating, and deleting records. To create a session, you need to import the sqlalchemy.orm.session.Session class and create an instance of it:
```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

```

Step 6: Adding Records

To add a new record to the database, you need to create a new instance of the model, add it to the session using the add method, and commit the session:

```
user = User(name='John Doe', age=30)
session.add(user)
session.commit()
```

Step 7: Querying Records

To retrieve records from the database, you can use the query method on the session:

```python
# Retrieve all records
users = session.query(User).all()

# Retrieve a single record
user = session.query(User).get(1)

# Print all users - one at a time
for user in users:
    print(user.id, user.name, user.age)


```



