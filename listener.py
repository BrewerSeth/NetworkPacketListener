#!/usr/bin/env python3
"""
Simple UDP packet listener
"""

import socket
import argparse


def listen(port, output_file=None):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Allow reuse of the port (fixes "Address already in use" error)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Enable receiving broadcast packets
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Bind to the specified port
    sock.bind(("0.0.0.0", port))

    print(f"Listening on UDP port {port}...")
    if output_file:
        print(f"Writing to {output_file}...")
    print("Press Ctrl+C to exit\n")

    try:
        while True:
            # Receive data (up to 1024 bytes)
            data, addr = sock.recvfrom(1024)
            utf8_str = data.decode("utf-8", errors="replace")
            hex_str = data.hex()

            # Format the output
            output = f"[{addr[0]}:{addr[1]}]\n  UTF-8: {utf8_str}\n  HEX:   {hex_str}\n"

            # Print to console
            print(output, end="")

            # Write to file if specified
            if output_file:
                with open(output_file, "a") as f:
                    f.write(output)
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
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output file to write packets to",
    )
    args = parser.parse_args()
    listen(args.port, args.output)
