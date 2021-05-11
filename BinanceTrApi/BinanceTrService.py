
from .BinanceTrRequests import sendRequest,sendRequestWithoutAuthorization
from .UserModel import UserModel as UM
from .Apihelpers import date_to_milliseconds
import json
import sys
import traceback
import os

class ApiService:
    """
    ApiServiceClass Object

    :param apiKey(str): Given account's api key.
    :param apiSecret(str): Given account's api secret key.
    """

    def __init__(self, apiKey, apiSecret):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.__constants()

    def __constants(self):
        current_dir = os.path.dirname(__file__)
        target_dir = os.path.abspath(os.path.join(current_dir, "constants.json"))

        with open(target_dir) as json_file:
            self.__constant = json.load(json_file)
        self.options = UM(self.apiKey, self.apiSecret)

    def testConnectivity(self):
        """
        Tests connectivity with server.

        :returns: (json) Return requested value from api.
        """
        try:
            result = sendRequestWithoutAuthorization("/open/v1/common/time", None, True)
            return result.json()

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getSymbol(self):
        """
        Fetchs market data.

        :returns: (json) Return requested value from api.
        """
        try:
            result = sendRequestWithoutAuthorization("open/v1/common/symbols", None, True)
            return result.json()

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getOrderBook(self, symbol, limit=100):
        """
        Get order book from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param limit(int): Give the limit to see how many order will be shown.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "limit": str(limit)}
            result = sendRequest("GET", "/open/v1/market/depth", params, True)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getRecentTrade(self, symbol, limit=500):
        """
        Get recent trades of given parity from market.

        :param symbol(str): Coin name with parity. ex. BTC_TRY
        :param limit(int): Number of recent trades to be returned.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "limit": str(limit)}
            result = sendRequestWithoutAuthorization("/trades", params)
            return result.json()

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getAggregateTrades(self, symbol, startDate=None, endDate=None, limit=50):
        """
        Get recent trades of given parity from market in given dates.

        :param symbol(str): Coin name with parity. ex. BTC_TRY
        :param startDate(str): Start date. ex.(5 min ago, 4 hour ago)
        :param endDate(str): End date. ex.(5 min ago, 4 hour ago)
        :param limit(int): Number of recent trades to be returned.

        :returns: (json) Return requested value from api.
        """
        try:
            timestamp = self.testConnectivity()["timestamp"]
            params = {"symbol": symbol, "limit": str(limit)}
            start_ts = None
            end_ts = None

            # if startDate:
            #     start_ts = date_to_milliseconds(startDate)
            # end_ts = None
            # if endDate:
            #     end_ts = date_to_milliseconds(endDate)
            #
            # if start_ts and end_ts:
            params["startTime"] = startDate
            params["endTime"] = endDate
            print(params)
            result = sendRequestWithoutAuthorization("/aggTrades", params)
            return result.json()

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getKline(self, symbol, interval, startDate=None, endDate=None, limit=500):
        """
        Get market data of given parity from market in given dates.

        :param symbol(str): Coin name with parity. ex. BTC_TRY
        :param startDate(str): Start date. ex.(5 min ago, 4 hour ago)
        :param endDate(str): End date. ex.(5 min ago, 4 hour ago)
        :param limit(int): Number of recent trades to be returned.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "limit": str(limit), "interval": interval}
            start_ts = None
            end_ts = None
            #
            # if startDate:
            #     start_ts = date_to_milliseconds(startDate)
            # end_ts = None
            # if endDate:
            #     end_ts = date_to_milliseconds(endDate)
            #
            if endDate and startDate:
                params["startTime"] = startDate
                params["endTime"] = endDate
            result = sendRequestWithoutAuthorization("/klines", params)
            return result.json()

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getAccountInformation(self):
        """
        Get account information.

        :returns: (json) Return requested value from api.
        """
        try:
            result = sendRequest("GET", "/open/v1/account/spot", self.options)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getAssetInformation(self, assetName):
        """
        Get asset information from account of given token.

        :param assetName(str): Coin name to fetch information.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"asset": assetName}
            result = sendRequest("GET", "/open/v1/account/spot/asset", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getOrderById(self, orderID):
        """
        Get order book by Id.

        :param orderID(str): Unique orderid taken from BinanceTr.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"orderID": orderID}
            result = sendRequest("GET", "/open/v1/orders/default", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getAllOpenOrders(self, symbol, limit=500):
        """
        Get all open orders from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param limit(int): Give the limit to see how many order will be shown.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "limit": str(limit), "type": self.__constant["AllOrders"]["Open"]}
            result = sendRequest("GET", "/open/v1/orders", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getAllOrders(self, symbol, limit=500):
        """
        Get all orders from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param limit(int): Give the limit to see how many order will be shown.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "limit": str(limit)}
            result = sendRequest("GET", "/open/v1/orders", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getAllOpenBuyOrders(self, symbol, limit=500):
        """
        Get all open buy orders from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param limit(int): Give the limit to see how many order will be shown.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "limit": str(limit), "type": self.__constant["AllOrders"]["Open"],
                      "side": self.__constant["OrderSide"]["BUY"]}
            result = sendRequest("GET", "/open/v1/orders", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def getAllOpenSellOrders(self, symbol, limit=500):
        """
        Get all open sell orders from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param limit(int): Give the limit to see how many order will be shown.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "limit": str(limit), "type": self.__constant["AllOrders"]["Open"],
                      "side": self.__constant["OrderSide"]["SELL"]}
            result = sendRequest("GET", "/open/v1/orders", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def postNewLimitOrder(self, symbol, side, origQuoteQuantity, price):
        """
        Post new limit order from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param side(str): BUY or SELL, usage with uppercase "BUY" "SELL".
        :param origQuoteQuantity(float): Quantity of coin for the order.
        :param price(int, float): Price count.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "side": self.__constant["OrderSide"][side],
                      "type": self.__constant["OrderTypes"]["Limit"], "quantity": str(origQuoteQuantity),
                      "price": str(price)}
            result = sendRequest("POST", "/open/v1/orders", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def postBuyMarketOrder(self, symbol, origQuantity):
        """
        Post buy market order from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param origQuoteQuantity(float): Quantity of coin for the order.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "side": self.__constant["OrderSide"]["BUY"],
                      "type": self.__constant["OrderTypes"]["Market"], "quoteOrderQty": str(origQuantity)}
            result = sendRequest("POST", "/open/v1/orders", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def postSellMarketOrder(self, symbol, origQuoteQuantity):
        """
        Post sell market order from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param origQuoteQuantity(float): Quantity of coin for the order.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"symbol": symbol, "side": self.__constant["OrderSide"]["SELL"],
                      "type": self.__constant["OrderTypes"]["Market"], "quantity": str(origQuoteQuantity)}
            result = sendRequest("POST", "/open/v1/orders", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def postStopLimitOrder(self, symbol, side, origQuoteQuantity, limitPrice, stopPrice):
        """
        Post stop limit orders from account.

        :param symbol(str): Coin name with parity. ex. BTC_TRY.
        :param side(str): BUY or SELL, usage with uppercase "BUY" "SELL".
        :param origQuoteQuantity(float): Quantity of coin for the order.
        :param limitPrice(int, float): Limit price count.
        :param stopPrice(int, float): Stop price count.

        :returns: (json) Return requested value from api.
        """

        try:
            params = {"symbol": symbol, "side": self.__constant["OrderSide"][side],
                      "type": self.__constant["OrderTypes"]["Limit"], "quantity": str(origQuoteQuantity),
                      "price": str(limitPrice), "stopPrice": str(stopPrice)}
            result = sendRequest("POST", "/open/v1/orders", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)

    def cancelOrderById(self, orderID):
        """
        Cancellation order by Id.

        :param orderID(str): Unique orderid taken from BinanceTr.

        :returns: (json) Return requested value from api.
        """
        try:
            params = {"orderId": str(orderID)}
            result = sendRequest("POST", "/open/v1/orders/cancel", self.options, params)
            return result

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errorDetails = "".join(traceback.format_exception(exc_type, exc_obj, exc_tb))
            print(errorDetails)