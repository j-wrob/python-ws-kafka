"""
Websocket Client module
"""
import asyncio
import ssl
import websockets

from websockets.exceptions import ConnectionClosed


class WebSocketClient:
    """
    Handles interaction with the WebSocket server, maintaining a persistent connection.
    """
    def __init__(self, websocket_url):
        self.websocket_url = websocket_url
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
        self.websocket = None

    async def connect(self):
        """
        Establishes the WebSocket connection.
        """
        self.websocket = await websockets.connect(self.websocket_url, ssl=self.ssl_context)

    async def send_message(self, message):
        """
        Sends a WebSocket message using the persistent connection.
        """
        if self.websocket is None:
            raise Exception("WebSocket connection not established. Call connect() first.")
        print(f"[WebSocket] Sending message: {message}")
        await self.websocket.send(message)
        return message

    async def read_response(self):
        """
        Receives first available WebSocket response using the persistent connection.
        """
        if self.websocket is None:
            raise Exception("WebSocket connection not established. Call connect() first.")
        response = await self.websocket.recv()
        print(f"[WebSocket] Received response: {response}")
        return response

    async def read_responses_amount(self, amount: int, timeout):
        """
        Receives given amount of available WebSocket responses using the persistent connection.
        """
        if self.websocket is None:
            raise Exception("WebSocket connection not established. Call connect() first.")
        responses_list = []
        for _ in range(amount):
            try:
                response = await asyncio.wait_for(self.websocket.recv(), timeout)
                responses_list.append(response)
            except TimeoutError:
                break
            except ConnectionClosed:
                print("[WebSocket] Connection closed. Stopping early.")
                break
        return responses_list

    async def close(self):
        """
        Closes the WebSocket connection.
        """
        if self.websocket is not None:
            await self.websocket.close()
            self.websocket = None