#!/usr/bin/env python
import pika
import psutil

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

while  (1):
	cpu_usage = psutil.cpu_percent(4)
	ram_usage = psutil.virtual_memory()[2]
	channel.queue_declare(queue='cpuusage')
	channel.queue_declare(queue='ramusage')
	channel.basic_publish(exchange='', routing_key='cpuusage', body= str(cpu_usage))
	channel.basic_publish(exchange='', routing_key='ramusage', body= str(ram_usage))
	print(" [x] Statistics Sent")
connection.close()
