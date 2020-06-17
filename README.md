# Socket-Programming-Quiz
A quiz based on Socket Programming in Python

This is a socket-based multiplayer quiz (on football) based on Python.

Instructions 
1.Download the files server.py and client.py 
2.Run this command on your terminal after going into the directory in which the files are stored python3 server.py <Your IP Address> <Any Port number>
3.Open three more terminals(three users) on your desktop and type python3 client.py <Your IP address> <Server's port number> and continue. You could alternatively do this on multiple systems instead of doing this on a single system.

Project Overview
There will be three players or participants in the game. The host (Server) has a list of 50 questions related to football and four options with correct answers with him/her. A question is randomly chosen among the given set of questions and then sends to all the three players. The players have to press the buzzer by pressing the enter key on the keyboard within 10 seconds. The first one to press the buzzer is given a chance to answer the question. If the answer is correct then he is awarded one point, else negative point of half awarded. The host then proceeds with the next question. The game stops when one of the players gets 5 points and then he is declared the winner.

Project Description
There are two parts in this Project:- Server and Client. MakeAllReady() function is used when all three players are connected to the Server and getting ready to play. Multi-Threading is used by the Server to handle all the clients at one time.

Clients use Multiplexing for I/O. The data from the Server gets printed in Clients' screen and the data from Clients get sent to Server. Select Module is used to run both the processes. And a lot of functions and modules are used for this Quiz.
