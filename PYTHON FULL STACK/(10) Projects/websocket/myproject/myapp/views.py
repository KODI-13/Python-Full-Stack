from django.shortcuts import render
from .pmClient import PMClient
import logging
from .websocket import PaytmWebSocketClient
# import pmclient
# Create your views here.

logging.basicConfig(level=logging.INFO)

class PaytmWebSocketClient:
    def __init__(self, token):
        self.token = token
        self.ws = None

    def on_message(self, message):
        logging.info(f"Received message: {message}")

    def on_error(self, error):
        logging.error(f"WebSocket error: {error}")

    def on_close(self, code, reason):
        logging.info(f"WebSocket closed: {code} - {reason}")

    def on_open(self):
        logging.info("WebSocket opened")

    def connect_to_websocket(self):
        # just have to Replace it with the actual endpoint and any other necessary configuration
        ws_url = "wss://paytm_money_api_url"                
        
        self.ws = PMClient.WebSocketApp(
            ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            header={"Authorization": f"Bearer {self.token}"}
        )

        self.ws.run_forever()



def home(request):
    # just have to replace 'token' with the actual token you receive for the day
    token = 'token'

    paytm_ws_client = PaytmWebSocketClient(token)
    paytm_ws_client.connect_to_websocket()
    return render(request,'myapp/home.html')
