"""
Websocket Client module
"""
import ssl
import websockets


class WebSocketClient:
    """
    Handles interaction with the WebSocket server.
    """
    def __init__(self, websocket_url):
        self.websocket_url = websocket_url
        # Setup SSL context to disable SSL verification
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

    async def send_message(self, message):
        """
        Sends a WebSocket message and returns both the sent and received messages
        """
        async with websockets.connect(self.websocket_url, ssl=self.ssl_context) as websocket:
            print(f"[WebSocket] Sending message: {message}")
            await websocket.send(message)

            # Await and return server response
            response = await websocket.recv()
            print(f"[WebSocket] Received response: {response}")
            return message, response
