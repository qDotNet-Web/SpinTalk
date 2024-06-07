let ws: WebSocket;

export const connect = (url: string) => {
  ws = new WebSocket(url);
    return ws;
};

export const disconnect = () => {
  ws.close();
};

export const send = (message: string) => {
  ws.send(message);
};

connect('ws://localhost:8000/ws');