# Apache Pulsar Quickstart

Apache Pulsar is an open-source, distributed, high-performance publish-subscribe messaging system that was created to handle large scale data streaming for big data use cases. It offers a range of features like at-least-once delivery, auto-failover, and multiple storage options. In this tutorial, we'll explore how to work with Apache Pulsar in Scala.

Prerequisites
Before getting started, you need to have the following software installed on your machine:

Scala 2.12 or higher
Apache Pulsar 2.5 or higher
SBT build tool
Step 1: Setting up the Project
First, create a new Scala project using SBT. You can do this by running the following command in the terminal:

```bash
sbt new scala/hello-world.g8
```

The above command will create a new Scala project with a default build.sbt file. Next, you need to add the following dependencies to your build.sbt file:

```bash
libraryDependencies += "org.apache.pulsar" % "pulsar-client" % "2.7.1"
```

Step 2: Creating a Pulsar Producer
A Pulsar producer is responsible for sending messages to a Pulsar topic. In this step, we'll create a Pulsar producer to send messages to a Pulsar topic.

```scala
import org.apache.pulsar.client.api._

object PulsarProducer {
  def main(args: Array[String]): Unit = {
    // Create a Pulsar client instance
    val client = PulsarClient.builder().serviceUrl("pulsar://localhost:6650").build()

    // Create a producer instance
    val producer = client.newProducer()
      .topic("my-topic")
      .create()

    // Send messages to the topic
    (1 to 100).foreach { i =>
      producer.send(s"message-$i")
    }

    // Close the client and producer instances
    producer.close()
    client.close()
  }
}

```
Step 3: Creating a Pulsar Consumer
A Pulsar consumer is responsible for consuming messages from a Pulsar topic. In this step, we'll create a Pulsar consumer to receive messages from a Pulsar topic.

```scala
import org.apache.pulsar.client.api._

object PulsarConsumer {
  def main(args: Array[String]): Unit = {
    // Create a Pulsar client instance
    val client = PulsarClient.builder().serviceUrl("pulsar://localhost:6650").build()

    // Create a consumer instance
    val consumer = client.newConsumer()
      .topic("my-topic")
      .subscriptionName("my-subscription")
      .subscribe()

    // Receive messages from the topic
    while (true) {
      val msg = consumer.receive()
      println(s"Received message: ${new String(msg.getData)}")
      consumer.acknowledge(msg)
    }

    // Close the client and consumer instances
    consumer.close()
    client.close()
  }
}

```

Step 4: Running the Application
Now that we