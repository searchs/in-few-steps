# Apache Impala: Create table from CSV file

In Apache Impala, you can create a table using a CSV file stored in Hadoop Distributed File System (HDFS). This can be useful when you have a large dataset stored in a CSV file that you want to analyze using Impala. In this tutorial, we will learn how to create a table using a CSV file on HDFS using Impala.

**_Prerequisites_**

Before we begin, make sure that you have installed the following on your system  via Cloudera Data Platform:

- Impala (version 3.0 or later)
- Impala Shell (impala-shell)
- Hadoop Distributed File System (HDFS)

## Uploading CSV File to HDFS

Before we can create a table using the CSV file, we need to upload the CSV file to HDFS. Let's assume that we have a CSV file named employees.csv on our local machine that we want to upload to HDFS. We can use the hadoop fs command to upload the file to HDFS. Run the following command in your terminal:

```bash
hadoop fs -put employees.csv /user/hive/warehouse/
```

This uploads the employees.csv file to the /user/hive/warehouse/ directory on HDFS.

## Creating a Table

To create a table using the CSV file, we use the CREATE TABLE statement with the STORED AS TEXTFILE clause. Let's create a table named employees with the following schema:

```sql
id INT, name STRING, age INT, salary FLOAT
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
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/warehouse/employees.csv';
```

This creates a table named employees with the specified schema and stores it as a text file.

## Querying Data

Now that we have created the table, we can query the data in the CSV file using Impala. Let's retrieve all the data from the employees table:

```sql
SELECT * FROM employees;
```

This retrieves all the data from the employees table.

## Conclusion

In this tutorial, we learned how to create a table using a CSV file on HDFS using Impala. We uploaded a CSV file to HDFS and then created a table using the CREATE TABLE statement with the STORED AS TEXTFILE clause. Impala is a powerful SQL query engine that can process and analyze large datasets stored in HDFS. With its support for HDFS and HBase, Impala is a great tool for data analysts and data scientists who need to analyze large datasets quickly and efficiently.
