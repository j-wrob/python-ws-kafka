import pytest
from ws_client import WebSocketClient

WEBSOCKET_URL = "wss://ws.postman-echo.com/raw"
MESSAGES = [
        "test_message_1",
        "test_message_2",
        "test_message_3"
    ]

@pytest.mark.asyncio
async def test_ws_multiple_messages():
    """
    Test websocket connection by sending and reading messages.
    Steps:
    - send 3 test messages
    - read up to 10 messages
    - verify that all test messages are received as response
    """
    ws_client = WebSocketClient(WEBSOCKET_URL)
    await ws_client.connect()
    for message in MESSAGES:
        await ws_client.send_message(message)

    all_responses = await ws_client.read_responses_amount(amount=10, timeout=10)

    for message in MESSAGES:
        assert message in all_responses

    await ws_client.close()