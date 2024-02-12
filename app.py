import time, os
from mcstatus import JavaServer

def get_server_status(server_address, server_port):
    server = JavaServer.lookup(server_address+":"+server_port)
    status = server.status()

    return {
        'latency': round(status.latency),
        'online_players': status.players.online,
        'max_players': status.players.max
    }

def display_server_status(server_address, server_port):
    while True:
        status = get_server_status(server_address, server_port)
        os.system("cls||clear")
        print(f"Status: {'Online' if status['latency'] is not None else 'Offline'}")
        print(f"Latency: {status['latency']} ms")
        print(f"Players: {status['online_players']}/{status['max_players']}")

        time.sleep(10)

server_address = input("Server Ip Address/Domain: ")
server_port = input("Port: ")

display_server_status(server_address, server_port)
