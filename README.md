# NetworkPacketListener

Simple UDP packet listener that prints incoming packets to the screen.

## What it does

Listens on UDP port 12321 and displays incoming packets in both UTF-8 and hexadecimal formats.

## How to run

```bash
python3 listener.py
```

Press `Ctrl+C` to exit.

## Testing

Send a test packet from another terminal:

```bash
echo "test message" | nc -u localhost 12321
```
