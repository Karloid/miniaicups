import json
import random

commands = ['left', 'right']
tick = 0
n = 30
parts = n / len(commands)
 
while True:
    z = input()
 
    choice = int(tick % n / parts)
    cmd = commands[choice]
    print(json.dumps({"command": cmd, 'debug': cmd}))
    tick += 1