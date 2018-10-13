#!/usr/bin/python
import logging
import argparse
from server import ServerMessageTypes, ServerComms
from statemachine import StateMachine

# Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true',
                    help='Enable debug output')
parser.add_argument('-H', '--hostname', default='127.0.0.1',
                    help='Hostname to connect to')
parser.add_argument('-p', '--port', default=8052,
                    type=int, help='Port to connect to')
parser.add_argument('-n', '--name', default='RandomBot', help='Name of bot')
args = parser.parse_args()

# Set up console logging
if args.debug:
    logging.basicConfig(
        format='[%(asctime)s] %(message)s', level=logging.DEBUG)
else:
    logging.basicConfig(format='[%(asctime)s] %(message)s', level=logging.INFO)


# Connect to game server
GameServer = ServerComms(args.hostname, args.port)

# Spawn our tank
logging.info("Creating tank with name '{}'".format(args.name))
GameServer.sendMessage(ServerMessageTypes.CREATETANK, {'Name': args.name})

state_machine = StateMachine(GameServer=GameServer, name=args.name)

# Main loop - read game messages, ignore them and randomly perform actions
i = 0
while True:
    message = GameServer.readMessage()
    state_machine.update(message)
    # attacking.aim_left()
    print(message)
