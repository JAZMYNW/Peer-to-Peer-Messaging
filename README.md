# Peer-to-Peer-Messaging

Implementation of a simple peer to peer messaging application that allows clients to communicate with eachother directly over the network.

## db-client
in_mess: Listens for incoming messages on specified port. Upon recieved connection starts new thread.
in_conn: Handles the incoming connections by receiving messages from the connected socket and printing it.
send: Sends message to specified IP address and port.
main: Prompts user to enter port then enters a loop of prompting for IP adress, port, and message.

## db-server
cc_database: Can create or connect to SQLite DB.
regclient: Registers client in database.
get_regclient: Retrieves client from DB.
main: Entry point to inititate server

## How to Run
-Run server in one terminal/first machine
-Run client, follow prompts to specify IP address and port number to connect to a peer


*implementation based on the tutorial provided in class
