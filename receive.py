#!/usr/bin/env python
import pika, sys, os

def checkutilization(usagestr):
   usage=float(usagestr)
   if usage<40:
   	print("Resource usage: Low\n")
   elif usage>=40 and usage<=60:
   	print ("Resource usage: Average\n")
   else:
   	print("Resource usage: High\n")
   return


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='cpuusage')
    channel.queue_declare(queue='ramusage')

    def callback(ch, method, properties, body):
        ram_usage=body.decode()
        print("CPU Usage (percentage): %r" % ram_usage)
        checkutilization(ram_usage)
   
    channel.basic_consume(queue='cpuusage', on_message_callback=callback, auto_ack=True)
    
    def callback(ch, method, properties, body):
        cpu_usage=body.decode()
        print("RAM Usage (percentage): %r" % cpu_usage)
        checkutilization(cpu_usage)
        
    channel.basic_consume(queue='ramusage', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for statistics from remote. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
                

