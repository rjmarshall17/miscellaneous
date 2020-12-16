#!/usr/bin/env python3

import socket
import sys
import time

if __name__ == '__main__':
    message = b'This is the message.  It will be repeated.'
    if len(sys.argv) > 1:
        message += b" Added: " + bytearray(sys.argv[1], 'utf-8')

    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = './.uds_socket'
    print('connecting to %s' % server_address)

    try:
        sock.connect(server_address)
    except socket.error as msg:
        print("Received a socket error on connect: %s" % msg)
        sys.exit(1)

    try:
        # Send data
        print('sending "%s"' % message)
        sock.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        print("The amount expected is: %d" % amount_expected)
        while amount_received < amount_expected:
            print("amount_received=%d" % amount_received)
            data = sock.recv(16)
            amount_received += len(data)
            print('received "%s"' % data)
    finally:
        sock.sendall(b'quit')
        time.sleep(2)
        print('closing socket')
        sock.close()