# Scott Ansman
# CNE 335 Winter
from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    my_server = Server("67.185.34.198")
    if my_server.ping():
        print("success")
    # TODO - Create a Server object
    # TODO - Call Ping method and print the results
