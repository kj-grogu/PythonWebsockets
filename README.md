## PythonWebsockets
POC on python web sockets with browsers + python clients

javascript<br/>
Python Modules <br/>
asyncio<br/>
websockets<br/>
json<br/>


# 
websocket handshake starts with a GET request on HTTP 1.1, if the server can support websockets the connection is upgraded to use websocket protocol and given a respose of 101 - Switching Protocols. Now the client and server can have bidirectional interaction (send each other messages) using a single TCP connection. Unlike in HTTP where the server can only respond if the client has made a request, in websockets the server can send back data to client as & when it wishes to. The underlying TCP connection can be closed by any party client/server. Very usefule for use cases like - Chatting, Live Feed, Multiplayer Gaming, Interactive Computing etc.   

