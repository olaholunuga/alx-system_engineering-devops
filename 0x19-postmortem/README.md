<img src=./image.gif width=50%>
# access loss to remote host name by remote host server 
Last week, when i was doing my webstack development project, i changed the file permissions of my remote server directory to 755.  unknown to me i had restricted the remote host from accessing the remote host name stored in a file in the root direct.

## Timeline
The error was realized on 10th February 1500 hours (West African Time) when i wanted to login into my remote host again that day.

## Root cause and resolution
 i wanted to installing the nginx webserver and write some text for the server to server to the public, i wanted to gain access to one of the files created by the nginx server but i was denied access so i tried to changed the  permission of the file but was denied access because it was in a directory i do not have access to, so i changed the the permissions of the root directory.
 i was able to edit the file, when i logedin again i was supprised to find "I don't have a name" where in the terminal, so i consulted stackoverflow to know thr what cause the behaviour, i was saw that it was because of my changing the permissions earlier.
 i was put through on how how to remedy the issue and i got through

## Measures against such problem in future
- always consult documentation before doing things on your own.
- and ofcourse don't do things on your whim
