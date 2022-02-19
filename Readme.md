# Serverless Computing Project

In IoT, in some cases, we need to monitor available devices in case of resource utilization, for further use-cases.

This simple IoT project (the producer) monitors RAM and CPU usage every 3 seconds and sends the related statistics to 2 different queues of the RabbitMQ message broker. Two queues are defined here, one for transmitting RAM usage and one for CPU usage (As demonstrated in the picture below). Then, the consumer picks these statistics from the corresponding queue and using a function, classifies their usage as "Low", "Average", or "High".


![alt text](C:\Users\sikandar\Desktop\serverless-producer-consumer-master\serverless-producer-consumer-master\images)
# Requirements

- Ubuntu 20.04
- Docker and Docker Compose 
- Nuclio
- RabbitMQ
- Python

# Installation
1. installing python
```
sudo apt install -y python3-pip
```
5. Installing required libraries (pika and psutil)
``` 
python3 -m pip install pika 
sudo pip install --upgrade psutil
````
3. Running docker containers of RabitMQ and Nuclio
``` 
sudo docker run -p 9000:15672  -p 1883:1883 -p 5672:5672  cyrilix/rabbitmq-mqtt 

sudo docker run -p 8070:8070 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp nuclio/dashboard:stable-amd64
```
4. Running Sender and Receiver functions
```
python3 send.py
python3 receive.py
```
- Note 1: `psutil` library of Python is used to measure the usage of main memory and CPU.
- Note 2: All the message transmission is done on the localhost
