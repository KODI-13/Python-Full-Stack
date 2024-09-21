document.addEventListener('DOMContentLoaded', function() {
    const socket = new WebSocket('ws://your-websocket-server-url');   // just have to provide websocket server url 

    socket.onopen = function(event) {
        console.log('WebSocket connection opened:', event);
    };

    socket.onmessage = function(event) {
        const dataDiv = document.getElementById('websocket-data');
        dataDiv.innerHTML = 'Received: ' + event.data;
    };

    socket.onclose = function(event) {
        console.log('WebSocket connection closed:', event);
    };

    // You can add code to send data to the server here

    window.addEventListener('beforeunload', function() {
        socket.close();
    });
});
