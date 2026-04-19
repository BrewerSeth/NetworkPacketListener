# NetworkPacketListener

Simple UDP packet listener that prints incoming packets to the screen.

## What it does

Listens on UDP and displays incoming packets in both UTF-8 and hexadecimal formats.

## How to run

```bash
python3 listener.py                 # Listen on default port 12321
python3 listener.py -p 5000         # Listen on port 5000
python3 listener.py --port 9999     # Listen on port 9999
```

Press `Ctrl+C` to exit.

## Options

- `-p, --port PORT`: UDP port to listen on (default: 12321)
