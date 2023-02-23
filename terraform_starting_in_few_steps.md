# Terraform - Starting in few steps
Terraform is an infrastructure-as-code (IaC) tool that enables users to create and manage their cloud infrastructure using a declarative language. It allows for the provisioning of resources across various cloud providers, including AWS, Google Cloud, and Microsoft Azure.

In this tutorial, we will cover the basics of Terraform, including installation, configuration, and resource provisioning.

_Prerequisites_
Before we begin, ensure that you have the following:

- An account with a cloud provider (AWS, Google Cloud, or Microsoft Azure)
- A command-line interface (CLI)
- A basic understanding of the infrastructure you want to create

**Installation**
To install Terraform, follow these steps:

- [ ] Visit the Terraform website and download the appropriate package for your operating system.
- [ ] Extract the downloaded package to a directory on your computer.
- [ ] Add the directory to your system's PATH environment variable to make the terraform executable available in your terminal.
Configuration
- [ ] The next step is to configure Terraform to interact with your cloud provider. To do this, you need to create a Terraform configuration file, which is written in Hashicorp Configuration Language (HCL). The configuration file should be named `main.tf`.

Here is an example of a basic Terraform configuration file:

```js
provider "aws" {
  access_key = "ACCESS_KEY"
  secret_key = "SECRET_KEY"
  region     = "REGION"
}

resource "aws_instance" "example" {
  ami           = "AMI_ID"
  instance_type = "INSTANCE_TYPE"
}
```

This configuration file specifies that we will be using AWS as our cloud provider, and it provisions an EC2 instance with the specified ami and instance_type.

To use this configuration file, run the following command in your terminal:

```bash
terraform init
```

This command initializes the working directory and downloads any necessary providers.

### Provisioning Resources

With the configuration file in place, we can now provision resources in our cloud provider. To do this, we use the terraform apply command.

```bash
terraform apply
```

This command creates the specified resources in your cloud provider. If you need to make changes to your configuration file, you can run terraform plan to preview the changes before applying them.

```bash
terraform plan
```

This command shows a preview of the changes that Terraform will make to your infrastructure.

**Conclusion**
In this tutorial, we covered the basics of Terraform, including installation, configuration, and resource provisioning. With this knowledge, you should be able to create and manage your cloud infrastructure using Terraform.