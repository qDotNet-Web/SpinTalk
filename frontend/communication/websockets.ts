let ws: WebSocket | null = null;

export const connect = (url: string) => {
  if (ws && ws.readyState === WebSocket.OPEN) {
    console.error("WebSocket is already connected");
    return;
  }
  ws = new WebSocket(url);
  ws.onerror = (event) => {
    console.error("WebSocket error:", event);
    ws.close();
  };
  ws.onclose = () => {
    console.log("WebSocket connection closed");
    ws = null;
  };
};

export const disconnect = () => {
  if (!ws || ws.readyState === WebSocket.CLOSED) {
    console.error("WebSocket is not connected");
    return;
  }
  ws.close();
};

export const send = (message: string) => {
  if (!ws || ws.readyState !== WebSocket.OPEN) {
    console.error("WebSocket is not connected");
    return;
  }
  ws.send(message);
};

export const receive = (onMessage: (message: string) => void) => {
  if (!ws || ws.readyState !== WebSocket.OPEN) {
    console.error("WebSocket is not connected");
    return;
  }
  ws.onmessage = (event) => {
    onMessage(event.data);
  };
  ws.onclose = () => {
    ws.onmessage = null;
  };
}

connect('ws://localhost:8000/ws');