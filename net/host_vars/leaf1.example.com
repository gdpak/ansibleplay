provider:
  host: "{{ inventory_hostname }}"
  username: ansible
  password: ansible
  use_ssl: no
  authorize: yes
  transport: cli

interfaces:
  - name: Ethernet1
    description: Link to Peer1
  - name: Ethernet2
    description: Link to Peer1
  - name: Loopback1000
    description: Loopback for BGP
  - name: Port-Channel50
    description: Peer Channel-group

