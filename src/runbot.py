#!/usr/bin/python
import logging
import argparse
import threading
from server import ServerMessageTypes, ServerComms
from statemachine import StateMachine
import time

# Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', action='store_true',
                    help='Enable debug output')
parser.add_argument('-H', '--hostname', default='127.0.0.1',
                    help='Hostname to connect to')
parser.add_argument('-p', '--port', default=8052,
                    type=int, help='Port to connect to')
parser.add_argument('-n', '--name', default='TimScorer', help='Name of bot')
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


lock = threading.Lock()


def recieve_messages():
    while True:
        message = GameServer.readMessage()
        lock.acquire()
        state_machine.update(message)
        lock.release()


def run_state_machine():
    while True:
        lock.acquire()
        state_machine.choose_state()
        state_machine.perform_current_state()
        lock.release()
        time.sleep(0.2)


message_thread = threading.Thread(target=recieve_messages)
message_thread.start()

state_machine_thread = threading.Thread(target=run_state_machine)
state_machine_thread.start()
