from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from app.utils import get_db_client
import json

client = get_db_client()


class TradeStreamAPI(APIView):
    """ return top 10 grate quantity trades """
    permission_classes = [permissions.AllowAny,]

    @staticmethod
    def update_keys(doc):
        doc['event_type'] = doc.pop('e')
        doc['event_time'] = doc.pop('E')
        doc['symbol'] = doc.pop('s')
        doc['trade_id'] = doc.pop('t')
        doc['price'] = doc.pop('p')
        doc['quantity'] = doc.pop('q')
        doc['buyer_order_id'] = doc.pop('b')
        doc['seller_order_id'] = doc.pop('a')
        doc['trade_time'] = doc.pop('T')

        return doc


    def get(self, request, symbol):

        db = client['finance']
        trades = db.trade_stream

        data = []
        for doc in trades.find({"s":symbol.upper()},{"_id":0}).sort("q",-1).limit(10):
            
            data.append(self.update_keys(doc))

        context = {
            "description":f"top 10 grate quantity trades on {symbol.upper()}",
            "data":data

        }
        return Response(context)
