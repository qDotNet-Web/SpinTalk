let ws: WebSocket;

export const connect = (url: string) => {
  ws = new WebSocket(url);
  console.log('Connecting to', url);
  ws.onopen = function(event) {
    console.log('Connection is open');
  };
  ws.onerror = function(error) {
    console.error(`WebSocket Error: ${JSON.stringify(error)}`);
  };
  ws.onclose = function(event) {
    console.log(`WebSocket closed: ${event.code} ${event.reason}`);
  };
    return ws;
};

export const disconnect = () => {
  ws.close();
};

export const send = (message: string) => {
  ws.send(message);
};


connect('ws://localhost:3000/ws');