import time
from mcstatus import MinecraftServer

def get_server_status(server_address, server_port):
    server = MinecraftServer(server_address, server_port)
    status = server.status()

    return {
        'latency': status.latency,
        'uptime': time.time() - status.created,
        'online_players': status.players.online,
        'max_players': status.players.max
    }

def display_server_status(server_address, server_port):
    while True:
        status = get_server_status(server_address, server_port)

        print(f"Status: {'Online' if status['latency'] is not None else 'Offline'}")
        print(f"Latency: {status['latency']} ms")
        print(f"Uptime: {status['uptime']:.2f} seconds")
        print(f"Players: {status['online_players']}/{status['max_players']}")

        time.sleep(10)

server_address = input("Server Ip Address/Domain: ")
server_port = int(input("Port: "))

display_server_status(server_address, server_port)
