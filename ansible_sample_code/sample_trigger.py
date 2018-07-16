#!/usr/bin/python

from trigger.acl import parse
import netaddr

def _create_packet_dict(self, cmd_out):
        lines = cmd_out.split('\n')
        start_rule = 0
        for index, line in enumerate(lines):
            try:
                p = parse(line)
            except Exception as e:
                continue
            if p.terms:
                match = p.terms[0].match
                for key in match:
                    if key == "source-address":
                        for m in match["source-address"]:
                            print (m)
                            v = netaddr.IPNetwork(str(m))
                            print (v[0])
                    if key == 'protocol':
                       for m in match["protocol"]:
                           print (type(m), dir(m), str(m))

                action = p.terms[0].action
                for a in action:
                    print (type(a))
                    print (a)


out = """
ip access-list extended ansible-ios
access-list 193 permit tcp 12.1.1.0 0.0.0.255 any eq www
access-list 193 permit tcp 12.1.1.3 0.0.0.0 any eq 443
"""

op = _create_packet_dict(None, out)
print (op)
