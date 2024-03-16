import os
import paramiko

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_file):
        self.server_ip = server_ip
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.key = paramiko.RSAKey.from_private_key_file(key_file)

    def ping(self):
        if os.system(f"ping -n 1 {self.server_ip}") == 0:
            return True
        else:
            return False

    def run_a_command(self, command):
        self.ssh.connect(hostname=self.server_ip, username="ubuntu", pkey=self.key)
        stdin, stdout, stderr = self.ssh.exec_command(command)
        line = stdout.readline()
        while line:
            print(line)
            line = stdout.readline()
        print(stderr.read().decode())
