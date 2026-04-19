#!/usr/bin/env python3
"""
Simple UDP packet listener on port 12321
"""

import socket


def listen():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to localhost on port 12321
    sock.bind(("0.0.0.0", 12321))

    print("Listening on UDP port 12321...")
    print("Press Ctrl+C to exit\n")

    try:
        while True:
            # Receive data (up to 1024 bytes)
            data, addr = sock.recvfrom(1024)
            print(f"[{addr[0]}:{addr[1]}] {data.decode('utf-8', errors='replace')}")
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        sock.close()


if __name__ == "__main__":
    listen()
