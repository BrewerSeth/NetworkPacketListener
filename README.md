# NetworkPacketListener

Simple UDP packet listener that captures and displays broadcast packets in both UTF-8 and hexadecimal formats.

## What it does

Listens on UDP for broadcast packets (sent to 255.255.255.255) and displays incoming packets with source address and both UTF-8 and hexadecimal representations.

## How to run

```bash
python3 listener.py                 # Listen on default port 12321
python3 listener.py -p 5000         # Listen on port 5000
python3 listener.py --port 9999     # Listen on port 9999
python3 listener.py -o packets.txt  # Listen and write to file
python3 listener.py -p 5000 -o output.txt  # Listen on port 5000, write to file
```

Press `Ctrl+C` to exit.

## Options

- `-p, --port PORT`: UDP port to listen on (default: 12321)
- `-o, --output FILE`: Output file to write packets to (appends to file)
