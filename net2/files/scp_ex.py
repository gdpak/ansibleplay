from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('ios02.example.net', username='ansible', password='ansible')

# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

scp.get('ios.cfg')

scp.close()
