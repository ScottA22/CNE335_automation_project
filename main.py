# Scott Ansman
# CNE 335 Winter
from Server import Server

def print_program_info():
    print("Server Automator v0.1 by Scott Ansman")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    my_server = Server("67.185.34.198")
    if my_server.ping():
        print("success")