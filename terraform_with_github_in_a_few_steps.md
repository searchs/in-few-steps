# Terraform in a few steps
Terraform is a powerful tool for infrastructure automation, and GitHub is one of the many providers that can be used with Terraform to manage your infrastructure as code. In this tutorial, we will walk through the process of setting up Terraform with GitHub as a provider.

_Prerequisites_
Before we start, you will need the following prerequisites:

- A GitHub account
- A Terraform CLI installed on your machine. You can download it from the official website at https://www.terraform.io/downloads.html


##### Step 1: Create a Personal Access Token on GitHub

To use Terraform with GitHub, you will need to create a personal access token on GitHub that Terraform can use to access your repositories. To create a personal access token, follow these steps:

- [ ] Log in to your GitHub account.
- [ ] Click on your profile picture in the top-right corner of the screen and select "Settings".
- [ ] Click on "Developer settings" in the left-hand menu, and then select "Personal access tokens".
- [ ] Click the "Generate new token" button.
- [ ] Give your token a descriptive name and select the appropriate scopes. For this tutorial, we will select the "repo" scope, which provides full access to private and public repositories.
- [ ] Click the "Generate token" button and copy the token to your clipboard.

##### Step 2: Create a New GitHub Repository
Next, we will create a new GitHub repository to store our Terraform configuration files. To create a new repository, follow these steps:

Log in to your GitHub account.
Click on your profile picture in the top-right corner of the screen and select "Your repositories".
Click the "New" button in the top-right corner of the screen.
Give your repository a descriptive name and optionally add a description.
Select "Private" or "Public" depending on your preferences.
Click the "Create repository" button.

##### Step 3: Create a Terraform Configuration File
Now that we have a GitHub repository to store our Terraform configuration files and a personal access token to authenticate with GitHub, we can create our first Terraform configuration file. In this example, we will create a simple configuration file that creates a new GitHub repository.

Create a new directory on your local machine and create a new file named `main.tf` inside the directory. Add the following code to the "main.tf" file:

```js
provider "github" {
  token = "YOUR_PERSONAL_ACCESS_TOKEN"
}

resource "github_repository" "example" {
  name = "example-repo"
  description = "An example repository created with Terraform"
  private = true
}
```

Replace "YOUR_PERSONAL_ACCESS_TOKEN" with the personal access token you created in Step 1.

##### Step 4: Initialize Terraform

Once you have created the Terraform configuration file, you need to initialize Terraform in the directory where the configuration file is located. To do this, open a terminal or command prompt and navigate to the directory where your `main.tf` file is located. Then, run the following command:

```bash
terraform init
```

This command will download and install the necessary provider plugins and initialize the Terraform working directory.

##### Step 5: Apply Terraform Configuration

Now that Terraform is initialized, you can apply the configuration and create the GitHub repository. Run the following command in your terminal:

```bash
terraform apply
```

Terraform will show you a plan of what it will do, and prompt you to confirm the changes. Type "yes" and hit enter to confirm.

Once the command completes, you should see output similar to the following:

```bash
Apply complete! Resources: 1 added, 0 changed, 0 destroyed
```