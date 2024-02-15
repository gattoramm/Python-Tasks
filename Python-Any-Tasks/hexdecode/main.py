#!/usr/bin/env python3
# frame = open("socket2", 'rb').read()
with open("socket2", 'rb').read() as frame:

    pos = 2
    if frame[1] == 254:
        pos += 2 # skip 2 bytes
    if frame[1] == 255:
        pos += 8 # skip 8 bytes

    # read the key (4 bytes)
    key = frame[pos:][:4]
    pos += 4

    # decode the payload
    payload = bytes(x ^ key[i % 4] for i, x in enumerate(frame[pos:]))

    # output
    print(payload.decode("utf-8"))
