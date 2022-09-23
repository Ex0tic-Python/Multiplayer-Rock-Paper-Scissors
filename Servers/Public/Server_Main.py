from threading import Thread
from socket import socket
from json import load, loads, dump, dumps


# Since there is no current way for Threads to communicate directly, I have to have communication be done through variables.


game_in_progress = False



# Handles connections and pre-game stuff. Also should handle Queue
def normal_game_connections(server_sock, server_data):
    server_sock.listen(7)
    

# Handles all game related stuff. Plays game, does after-game stuff
def normal_game_logic(server_sock):
    pass

# Simple. Just contains functions and an infinite loop. Doesn't do anything.
def normal_game_client(server_sock, server_data):
    pass

def find_server():
    # Retrieve server list JSON
    with open("Data.json", "r") as json_file:
        servers_json = load(json_file)
        
    # Find an offline server and assign it's key to 'server_key'. Returns None if no server is offline
    server_key = None
    for key in range(1, 7):
        if servers_json[key]["Online"] == False:
            server_key = key
            break
    if server_key is None:
        return None

    # Should a server be found, mark the server as online and return the server info
    servers_json[server_key]["Online"] = True
    with open("Data.json", "w") as json_file:
        dump(json_file, servers_json)
    return servers_json[server_key].pop("Online")


if __name__ == "__main__":
    returned_data = find_server()
    if returned_data is not None:
        server_sock = socket()
        print(f"""
Server setup and ready to go!
Server Name: {returned_data['Server Name']}
Server Dedicated Game-Mode: {returned_data['Game Mode']}
IP Address: {returned_data['Address'][0]}
Port Number: {returned_data['Address'][0]}
        """)
        server_sock.bind(tuple(returned_data["Address"]))
        game_modes_dict[game_mode](server_sock, returned_data)
    else:
        print("No servers offline. Shutting down...")
