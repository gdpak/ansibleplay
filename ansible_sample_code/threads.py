#!/usr/bin/env python

import sys
import time
import os
from Queue import Queue
from threading import Thread
import threading


def delayed():
    print('delaying thread')

def command_handler(q):
    arg_list = q.get()
    print (arg_list[0])
    if arg_list[0] == "version":
        print('Version 999')
        print('Cisco 3745 (R7000) processor (revision 2.0) with 245760K/16384K bytes of memory.')
        print('Cisco IOS XE Software, Version 03.16.07b.S - Extended Support Release')
        print(threading.current_thread().getName(), 'Starting')
        with open('/tmp/t1', 'r') as f:
            a = f.read()
            while a != '1':
               a = f.read()

        print(threading.current_thread().getName(), 'Exit')

    elif arg_list[0] == "running-config":
        #print('Building configuration...')
        #print('')
        #print('Current configuration : 184 bytes')
        #print('!')
        print('interface GigabitEthernet0/0')
        print(' description Gigabit0')
        print(' no ip address')
        print(' load-interval 30')
        with open('/tmp/t1', 'w') as f:
           f.write('1')

        print(' duplex full')
        print(' speed 100')
        print(' pppoe enable group global')
        print(' pppoe-client dial-pool-number 10')
        print('end')
    elif ' '.join(arg_list[0:3]) == "ip interface brief":
        print('Interface     IP-Address     OK?  Method  Status                  Protocol')
        print('Ethernet0     10.108.00.5    YES  NVRAM   up                      up      ')
        print('Ethernet1     unassigned     YES  unset   administratively down   down    ')
        print('Loopback0     10.108.200.5   YES  NVRAM   up                      up      ')
        print('Serial0       10.108.100.5   YES  NVRAM   up                      up      ')
        print('Serial1       10.108.40.5    YES  NVRAM   up                      up      ')
        print('Serial2       10.108.100.5   YES  manual  up                      up      ')
        print('Serial3       unassigned     YES  unset   administratively down   down    ')

    sys.exit(0)

def main():
    q = Queue()
    nworkers = 3

    if sys.argv[1] == 'version':
       q.put(["version"])
    elif sys.argv[1] == 'running-config':
       q.put(["running-config"])
    elif ' '.join(sys.argv[1:3]) == "ip interface brief" :
       q.put([ sys.argv[1], sys.argv[2], sys.argv[3] ])

    t1= Thread(target=command_handler, args=(q,))
    t2= Thread(target=command_handler, args=(q,))
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()
    t1.join()

if __name__ == "__main__":
    main()

