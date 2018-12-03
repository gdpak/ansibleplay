from scapy.all import *

A = '12.1.1.4' # spoofed source IP address
B = '216.58.196.174' # destination IP address
C = 10000 # source port
D = 20000 # destination port
payload = "yada yada yada" # packet payload

#spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
frame = IP(src=A)
frame.dst=B
tcp = TCP(dport=D)
frame = frame / tcp
frame.show()
print (conf.route)
conf.route.add(host=B, gw='12.1.1.20', dev='enp0s16')
print (conf.route)
send(frame)
