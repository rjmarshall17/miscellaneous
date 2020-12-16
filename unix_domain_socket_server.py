#!/usr/bin/env python3

import os
import socket
import asyncio

"""
This challenge tests your understanding of Sockets and Multi-Threaded programming.

Your task is to write a UNIX Domain Socket(UDS) server which can accept connection from 'N' clients.
Each client will send text data over the socket. Read the data and send it back to the client. The 
server should be Multi-Threaded and should service all clients in parallel.

To support Multi-Threading you can use the POSIX thread library (C,C++) or the default threading library
for other languages.

Communication Protocol

Read data from client and send the response back.
String "END" marks end of communication from a client. Send response "END" and disconnect the client.

Example request 1:

Client 1:
Hello World
END
Example response 1:

Client 1:
Hello World
Example request 2:

Client 2:
This is line 1
This is line 2
END
Example response 2:

Client 2:
This is line 1
This is line 2
"""

server_address = './.uds_socket'

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Set up the asyncio event loop
loop = asyncio.get_event_loop()

# Set up the Unix Domain Socket server
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(server_address)
server.listen()
server.setblocking(False)


async def handle_client(client):
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        print("server received: %s" % str(request))
        response = str(request)
        try:
            await loop.sock_sendall(client, response.encode('utf8'))
        except BrokenPipeError:
            print("Broken pipe")
            break
    client.close()
    print('='*80)


async def run_server():
    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))


if __name__ == '__main__':
    print("Starting the server")
    loop.run_until_complete(run_server())

