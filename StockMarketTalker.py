'''
    Created on 20th March by Vaibhav

    Purpose:- This file is first of all a blueprint. Its actual implementation will be provided in some base classes.
              The purpose is to act as a link between our agents (trading algorithms) and stock market. But predominantly, this class is meant to be used by the agent.
              The agent will be able to ask information like stock price, given stock name or stock code, to place order to buy a certain quantity of a stock and related stuff.
              If in future, there is a decision to defer from this purpose, it should be documented here.
'''


class StockMarketTalker:

    def getStockPrice(stockCode):
        raise NotImplementedError
        
    def buyStock(stockCode, quantity):
        raise NotImplementedError
        
    def sellStock(stockCode, quantity):
        raise NotImplementedError
