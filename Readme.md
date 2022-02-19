# Serverless Computing Project

In the IoT, we sometimes need to keep an eye on accessible devices to see whether they're being used for other purposes.

This basic IoT project (the producer) checks RAM and CPU use every three seconds and transmits the data to two RabbitMQ message broker queues. Here, two queues are established, one for communicating RAM utilization and the other for transmitting CPU usage (As demonstrated in the picture below). The consumer then selects these statistics from the associated queue and categorizes their use as "Low," "Average," or "High" using a function.


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
