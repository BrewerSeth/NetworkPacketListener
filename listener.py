#!/usr/bin/env python3
"""
Simple UDP packet listener
"""

import socket
import argparse


def listen(port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the specified port
    sock.bind(("0.0.0.0", port))

    print(f"Listening on UDP port {port}...")
    print("Press Ctrl+C to exit\n")

    try:
        while True:
            # Receive data (up to 1024 bytes)
            data, addr = sock.recvfrom(1024)
            utf8_str = data.decode("utf-8", errors="replace")
            hex_str = data.hex()
            print(f"[{addr[0]}:{addr[1]}]")
            print(f"  UTF-8: {utf8_str}")
            print(f"  HEX:   {hex_str}\n")
    except KeyboardInterrupt:
        print("\nShutting down...")
    finally:
        sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Listen to UDP packets")
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=12321,
        help="UDP port to listen on (default: 12321)",
    )
    args = parser.parse_args()
    listen(args.port)
