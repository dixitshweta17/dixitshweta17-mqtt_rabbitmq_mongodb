## Prerequisites

- Windows operating system
- Administrator access
- Erlang/OTP installed
- RabbitMQ installed

# RabbitMQ Setup with Management Plugin on Windows

Do the RabbitMQ Setup

## Installation Steps

### 1. Install Erlang/OTP

1. Download and install Erlang/OTP from the [Erlang website](https://www.erlang.org/downloads).
2. During installation, note the installation directory (e.g., `C:\Program Files\Erlang OTP`).

### 2. Install RabbitMQ

1. Download and install RabbitMQ from the [RabbitMQ website](https://www.rabbitmq.com/install-windows.html).
2. During installation, note the installation directory (e.g., `C:\Program Files\RabbitMQ Server\rabbitmq_server`).

## 3. Set `ERLANG_HOME` Environment Variable

1. Open the Start menu, search for "Environment Variables", and select "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables" button.
3. Under "System variables", click "New" to create a new environment variable.
4. Set the variable name to `ERLANG_HOME` and the variable value to the Erlang installation directory (e.g., `C:\Program Files\Erlang OTP`).
# manually add: set ERLANG_HOME=C:\Program Files\Erlang OTP

## Add Erlang to the `PATH` Environment Variable
1. In the Environment Variables window, under "System variables", find the `Path` variable and select it, then click "Edit".
2. Add a new entry with the path to the `bin` directory inside your Erlang installation directory (e.g., `C:\Program Files\Erlang OTP\bin`).
#manually add: set PATH=%PATH%;C:\Program Files\Erlang OTP\bin


## 5.RabbitMQ Credentials

Navigate to http://localhost:15672
Log in with the default credentials:
Username: guest
Password: guest


## 6. Project Structure:
Client.py: Publish msg to que
Server.py: Consume mst from que
app.py: handle status count (http://127.0.0.1:5000/status_count?start=2024-07-18T00:00:00&end=2024-07-18T23:59:59)