import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        if os.system(f"ping -n 1 {self.server_ip}") == 0:
            return True
        else:
            return False
