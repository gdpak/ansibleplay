import paramiko
import logging
from paramiko.common import DEBUG
from paramiko.common import INFO

def log_to_file(filename, level=INFO):
    """send paramiko logs to a logfile,
    if they're not already going somewhere"""
    l = logging.getLogger("paramiko")
    if len(l.handlers) > 0:
        return
    l.setLevel(level)
    f = open(filename, "a")
    lh = logging.StreamHandler(f)
    frm = "%(levelname)-.3s [%(asctime)s.%(msecs)03d] thr=%(_threadid)-3d"
    frm += " %(name)s: %(message)s"
    lh.setFormatter(logging.Formatter(frm, "%Y%m%d-%H:%M:%S"))
    l.addHandler(lh)

user = raw_input('Username: ')
password = raw_input('Password: ')
name = raw_input('Hostname: ')
command = raw_input('Command: ')

nbytes = 4096
log_to_file("./ssh_logs.txt")

ssh = paramiko.Transport((name, 22))
ssh.connect(username=user, password=password)
stdout_data = []
stderr_data = []
session = ssh.open_channel(kind='session')
session.exec_command(command)
while True:
    if session.recv_ready():
        stdout_data.append(session.recv(nbytes))
    if session.recv_stderr_ready():
        stderr_data.append(session.recv_stderr(nbytes))
    if session.exit_status_ready():
        break

print 'exit status: ', session.recv_exit_status()
print ''.join(stdout_data)
print ''.join(stderr_data)

session.close()
ssh.close()
