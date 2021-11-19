"""
Rules for BattleShip (a Milton Bradley Game)
Game Objective
The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates.  Neither you nor the other player can see the other's board so you must try to guess where they are.  Each board in the physical game has two grids:  the lower (horizontal) section for the player's ships and the upper part (vertical during play) for recording the player's guesses.

Starting a New Game
Each player places the 5 ships somewhere on their board.  The ships can only be placed vertically or horizontally. Diagonal placement is not allowed. No part of a ship may hang off the edge of the board.  Ships may not overlap each other.  No ships may be placed on another ship.

Once the guessing begins, the players may not move the ships.

The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).

Playing the Game
Player's take turns guessing by calling out the coordinates. The opponent responds with "hit" or "miss" as appropriate.  Both players should mark their board with pegs:  red for hit, white for miss. For example, if you call out F6 and your opponent does not have any ship located at F6, your opponent would respond with "miss".  You record the miss F6 by placing a white peg on the lower part of your board at F6.  Your opponent records the miss by placing.

When all of the squares that one your ships occupies have been hit, the ship will be sunk.   You should announce "hit and sunk".  In the physical game, a red peg is placed on the top edge of the vertical board to indicate a sunk ship.

As soon as all of one player's ships have been sunk, the game ends.
"""

import random
import socket
import time

# Messages
HIT = "HIT"
MISS = "MISS"
QUIT = "QUIT"

HOST, PORT = '192.168.228.52', 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

connections, addresses, points = [], [], []

turn = random.randint(0, 1)


def otherPlayer():
    global turn
    if turn == 0:
        return 1
    else:
        return 0


def getPlayers():
    while len(connections) < 2:
        communication_socket, address = server.accept()
        print(f"Connection received/nCommunication Socket: {communication_socket}/nAddress: {address}")
        connections.append(communication_socket)
        addresses.append(address)
        points.append(17)

        message = communication_socket.recv(1024).decode('utf-8')
        print(message)
    return True


while True:
    if getPlayers():
        # Player whose turn is it
        player_turn = connections[turn]

        # Other player who is waiting
        other_player = connections[otherPlayer()]

        # Message to player telling that it is your turn
        player_turn.send("Your turn".encode('utf-8'))

        # if player responds with hit
        if player_turn.recv(1024).decode('utf-8') == HIT:
            # take points from other player
            points[otherPlayer()] -= 1

            # Send appropriate messages to each player
            player_turn.send("That was a hit on enemy".encode('utf-8'))
            other_player.send("Enemy hit you".encode('utf-8'))

        # if player responds with miss
        elif player_turn.recv(1024).decode('utf-8') == MISS:

            # Send appropriate messages to each player
            player_turn.send("You missed".encode('utf-8'))
            other_player.send("Enemy missed. Lucky You".encode('utf-8'))

        elif player_turn.recv(1024).decode('utf-8') == QUIT:
            other_player.send("Your opponent quit".encode('utf-8'))

            connections.pop(turn)
            addresses.pop(turn)
            points.pop(turn)

        turn = 1 if 0 else 0
