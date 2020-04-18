'''
Purpose - After getting the stock price, this file will use the algorithm to cal
culate and trade the stock
'''


class Agent:                # Assuming we know which stock we are buying
    
    def __init__(self, stockName):
        self.stockName = stockName
        self.basePrice = None
        self.buyPrice = None
        self.maxPrice = None

        self.currStatus = "SOLD"

        self.maxProfitPct = 0.03
        self.minProfitPct = 0.005
        self.buyPricePct = 0.005


    def getStockName(self):
        return self.stockName

    def getCurrStatus(self):
        return self.currStatus
        

    def getStopLoss(self, buyPrice, maxPrice):
        ''' If an appropriate base price is set, returns correct stopLoss according to our algo, else returns None '''
        ''' We currently have 3 slabs for calculation of stopLoss '''
        if buyPrice is None or maxPrice is None: return None
        profitPct = (maxPrice - buyPrice) / buyPrice
        if profitPct < self.minProfitPct:
            pct = 0.003
        elif profitPct > self.maxProfitPct:
            pct = profitPct - 0.01
        else:
            pct = profitPct / 4
        return (1 - pct) * maxPrice


    def getBuyPrice(self, basePrice):
        if basePrice is None: return None
        return (1 + self.buyPricePct) * basePrice
    

    def sell(self, stockPrice):
        self.basePrice = stockPrice
        self.buyPrice = None
        self.maxPrice = None
        self.currStatus = "SOLD"


    def buy(self, stockPrice):
        self.buyPrice = stockPrice
        self.maxPrice = stockPrice
        self.currStatus = "BOUGHT";

    
    def getAction(self, stockPrice):
        ''' Returns SELL, BUY or HOLD, number of stocks and Stoploss using algorithm '''
        assert stockPrice >= 0
        
        if self.currStatus == "SOLD":
            if self.basePrice is None or self.basePrice > stockPrice:
                self.basePrice = stockPrice
                return "HOLD"
            elif stockPrice >= self.getBuyPrice(self.basePrice):
                self.buy(stockPrice)
                return "BUY"
            else:
                return "HOLD"


        else:   # Current State is BOUGHT
            self.maxPrice = max(self.maxPrice, stockPrice)
            if self.getStopLoss(self.buyPrice, self.maxPrice) >= stockPrice:
                self.sell(stockPrice)
                return "SELL"
            else:
                return "HOLD"
