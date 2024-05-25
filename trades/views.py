from django.http import HttpResponse
from tradewise.mongo_client import db

def index(request):
    trades_collection = db.trades
    trade = {
        "user": "example_user",
        "trade_details": "example_trade"
    }
    trades_collection.insert_one(trade)
    trades = list(trades_collection.find())
    return HttpResponse(f"Hello, world. You're at the trades index. Current trades: {trades}")