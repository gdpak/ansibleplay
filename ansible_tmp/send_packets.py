from scapy.all import *

A = '12.1.1.4' # spoofed source IP address
B = '11.1.1.3' # destination IP address
C = 10000 # source port
D = 20000 # destination port
payload = "yada yada yada" # packet payload

spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
send(spoofed_packet)
