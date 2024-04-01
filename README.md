# Pytest Automation Framework Guide

Welcome to our Pytest Automation Framework! This guide is designed for anyone, regardless of their technical background, to set up and run automated tests. We've made the process as simple as possible, guiding you step by step.

## Prerequisites

Before you start, you'll need the following:

- **Python**: If you haven't installed Python yet, head over to the [Python official website](https://www.python.org/downloads/) and follow the instructions for your operating system.
- **Docker**: Docker allows us to run our applications in containers, making sure the environment is the same no matter where it runs. Download it from [Docker's official website](https://www.docker.com/).

## Setup Guide

### 1. Installing Requirements

First, we need to install some Python libraries that our tests depend on:

1. Open your terminal or command prompt.
2. Navigate to the folder where you've saved our project.
3. Run `pip install -r requirements.txt` to install the necessary Python packages.

### 2. Understanding Docker Compose

Docker Compose is a tool that allows us to define and run multi-container Docker applications. For our project:

- **WordPress and a Database**: We've set up a WordPress site with a connected database, ready for testing.
- **Report Portal**: This is where you'll see the results of the tests. It's already configured with projects, users, API keys, and everything else needed.

### 3. Running Docker Compose

To prepare our test environment:

1. In the same terminal window, make sure you're in the project folder.
2. Type `docker-compose up` and press Enter. This command sets up the WordPress site and Report Portal by starting the necessary containers.

### 4. Insert Users Script

Next, we need to populate Report Portal with user data:

1. There's a script that does this automatically. Based on whether you're on Windows, macOS, or Linux, you'll run a specific command. (We'll ensure this command is clear in the final README.md)

### 5. Running the Tests

Now, everything is ready for you to run the tests:

1. In your terminal, staying in the project folder, type `pytest --reportportal`.
2. Press Enter. The tests will execute, and the results will be sent to Report Portal.

### Report Portal Access

After the tests are complete, you can view the results in Report Portal:

- **URL**: (You'll provide the specific URL here)
- **Username**: python.pytest
- **Password**: Pass1234!

## Conclusion

That's all! You've successfully set up and run your tests. If you face any issues or have questions, we're here to help.
