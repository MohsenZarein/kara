from celery import shared_task
import websocket, json
from pymongo import MongoClient
from datetime import datetime


@shared_task
def get_trade_stream_data():

    client = MongoClient(
        host='localhost',
        port=27017
    )
    db = client['finance']
    trades = db.trade_stream


    def on_message(wsapp, data):
        d = json.loads(data)
        unix_event_time = d['E'] / 1000
        unix_trade_time = d['T'] / 1000
        d.update(
            {
                'E':datetime.utcfromtimestamp(unix_event_time),
                'T':datetime.utcfromtimestamp(unix_trade_time)
            }
        )
        trades.insert_one(d)


    def on_error(wsapp, err):
        print("got an error", err)
        wsapp.close()
        client.close()


    def on_close(wsapp):
        print("connection closed !")
        wsapp.close()
        client.close()

    wsapp = websocket.WebSocketApp(
        "wss://stream.binance.com:9443/ws/btcusdt@trade",
        on_message=on_message,
        on_close=on_close, 
        on_error=on_error
    )
    
    wsapp.run_forever()