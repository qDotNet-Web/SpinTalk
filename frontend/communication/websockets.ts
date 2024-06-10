/*let ws: WebSocket;

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

connect('ws://localhost:8000/ws');*/

let ws: WebSocket | null = null;

export const connect = (url: string) => {
  if (ws && ws.readyState === WebSocket.OPEN) {
    console.error("WebSocket is already connected");
    return;
  }
  ws = new WebSocket(url);
  ws.onerror = (event) => {
    console.error("WebSocket error:", event);
  };
  ws.onclose = () => {
    console.log("WebSocket connection closed");
  };
};

export const disconnect = () => {
  if (!ws || ws.readyState!== WebSocket.OPEN) {
    console.error("WebSocket is not connected");
    return;
  }
  ws.close();
};

export const send = (message: string) => {
  if (!ws || ws.readyState!== WebSocket.OPEN) {
    console.error("WebSocket is not connected");
    return;
  }
  ws.send(message);
};

connect('ws://localhost:8000/ws');