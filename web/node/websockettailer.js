// Node.js WebSocket server script
const http = require('http');
const WebSocketServer = require('websocket').server;
const server = http.createServer();
server.listen(9898);
const wsServer = new WebSocketServer({
	httpServer: server
});

const Journalctl = require('journalctl');
const journalctl = new Journalctl({unit: 'eyesy-python.service'});
wsServer.on('request', function(request) {
    const connection = request.accept(null, request.origin);
	connection.on('message', function(message) {
	console.log('Received Message:', message.utf8Data);
	connection.sendUTF('connected to websocket server');
     
   journalctl.on("event", function(event) {
	   connection.sendUTF(event.MESSAGE);
   });


   
    });
	connection.on('close', function(reasonCode, description) {
		console.log('Client has disconnected.');
	});
});

wsServer.on('connection', function(ws) {
    console.log('connection !');

    connection.sendUTF('Hi SERVER here');

    //ws.timer=setInterval(function(){pingpong(ws);},1000);

});
