# Docker with java application and mysql


Docker is a platform that allows you to easily create, deploy, and run applications in containers. Containers are isolated environments that allow you to run your applications in a consistent and reproducible manner, regardless of the underlying infrastructure. In this tutorial, we will create a simple Java application that communicates with a MySQL database and run it in a Docker container.

1. Installing Docker:
To get started with Docker, you need to install it on your machine. You can download the Docker Community Edition (CE) from the official Docker website (https://www.docker.com/products/docker-desktop). Docker CE is free and available for Windows, MacOS, and Linux.

2. Setting up a Java application:
For this tutorial, we will create a simple Java application that connects to a MySQL database and retrieves data from it. The application will consist of two classes:
    - A database connection class that will handle the database connection.
    - A main class that will retrieve the data from the database and display it.
3. Creating a Dockerfile:
A Dockerfile is a script that contains instructions for building a Docker image. In our case, the Docker image will contain our Java application and the MySQL database. To create a Dockerfile, follow these steps:
Create a new file in the root directory of your Java project called “Dockerfile”.
Add the following code to the Dockerfile:

```Dockerfile
FROM java:8
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD ["java", "-jar", "your-jar-file-name.jar"]

```

The Dockerfile is used to build the Docker image that contains our Java application. The first line specifies the base image to use (in this case, a Java 8 image). The WORKDIR instruction sets the working directory for the rest of the instructions in the Dockerfile. The COPY instruction copies all the files in the current directory to the working directory in the Docker image. The EXPOSE instruction tells Docker to expose port 8080, which will be used by the Java application. The CMD instruction specifies the command to run when the Docker container is started. In this case, we run the Java application by executing the java -jar command with the name of our JAR file.

4. Building the Docker image:
With the Dockerfile in place, we can now build the Docker image. Open a terminal window and navigate to the root directory of your Java project. Then run the following command:
    
```bash

docker build -t your-image-name .
```

The -t flag is used to specify the name of the Docker image, and the . at the end of the command specifies the current directory as the build context. This tells Docker to build an image using the Dockerfile in the current directory.

5. Running the Docker container:
With the Docker image built, we can now run the Docker container. To do this, we will use the following command:

```shell
docker run -p 8080:8080 your-image-name
```

The -p flag maps the host port 8080 to the container port 8080, which allows us to access the Java application from our host machine. The your-image-name argument specifies the name of the Docker image to run.

6. Setting up the MySQL database:
Now that the Java application is running in a Docker container, we need to set up the MySQL database. To do this, we will create another Docker container that runs the MySQL database.
