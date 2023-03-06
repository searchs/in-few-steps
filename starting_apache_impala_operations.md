# Apache Impala CRUD operations
Apache Impala is an open-source massively parallel processing SQL query engine for processing and analyzing large datasets in real-time. It was developed by Cloudera and is based on Google's Dremel paper. Impala supports SQL-like queries and works seamlessly with Hadoop Distributed File System (HDFS) and Apache HBase. In this tutorial, we will learn how to perform CRUD (Create, Read, Update, Delete) operations using Impala.

**_Prerequisites_**
Before we begin, make sure that you have installed the following on your system via Cloudera Data Platform:

- Impala (version 3.0 or later)
- Impala Shell (impala-shell)
- Hadoop Distributed File System (HDFS)

## Connecting to Impala

To connect to Impala, open the Impala Shell by running the following command in your terminal:

```bash
impala-shell
```

You will see the Impala Shell prompt:

```bash
[quickstart.cloudera:21000] >
#Type quit; to exit the Impala Shell.
```

## Creating a Table

To create a table in Impala, we use the CREATE TABLE statement. Let's create a table named employees with the following schema:

```sql
id INT, 
name STRING, 
age INT, 
salary FLOAT
```

To create the table, run the following command in the Impala Shell:

```sql
CREATE TABLE employees (
    id INT,
    name STRING,
    age INT,
    salary FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

This creates an empty table with the specified schema.

## Inserting Data

To insert data into the table, we use the INSERT INTO statement. Let's insert some data into the employees table:

```sql
INSERT INTO employees VALUES
    (1, 'John Doe', 30, 50000.0),
    (2, 'Jane Smith', 25, 45000.0),
    (3, 'Bob Johnson', 35, 60000.0),
    (4, 'Mary Brown', 28, 55000.0);
```

This inserts four rows of data into the employees table.

## Retrieving Data

To retrieve data from the table, we use the SELECT statement. Let's retrieve all the data from the employees table:

```sql
SELECT * FROM employees;
```

This retrieves all the data from the employees table.

## Updating Data
 
To update data in the table, we use the UPDATE statement. Let's update the salary of the employee with id 1 to 55000.0:

```sql
UPDATE employees SET salary = 55000.0 WHERE id = 1;
-- This updates the salary of the employee with id 1 to 55000.0.
```

## Deleting Data

To delete data from the table, we use the DELETE FROM statement. Let's delete the employee with id 2:

```sql
DELETE FROM employees WHERE id = 2;
-- This deletes the employee with id 2 from the employees table.
```

## Conclusion

In this tutorial, we learned how to perform CRUD operations using Impala. We created a table, inserted data, retrieved data, updated data, and deleted data. Impala is a powerful SQL query engine that can process and analyze large datasets in real-time. With its support for HDFS and HBase, Impala is a great tool for data analysts and data scientists who need to analyze large datasets quickly and efficiently.
