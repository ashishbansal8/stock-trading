''' 
	Created on 20th March by Vaibhav

	Purpose:- This file is an implementation class for StockMarketTalker.
			  It uses bsedata module to get information from stock market
'''

from bsedata.bse import BSE
import time
import random

from StockMarketTalker import StockMarketTalker


class RandomStockMarketTalker(StockMarketTalker):


	def __init__(self):
		super(RandomStockMarketTalker, self).__init__()
		self.basePrice = 1000
		self.currPrice = self.basePrice
		self.MIN_TIME_BW_REQUESTS = 0	# So that we don't get banned by servers of BSE
		self.std = 2

	def getRequestInterval(self):
		return self.MIN_TIME_BW_REQUESTS

	def getStockInfo(self, stockName):
		''' Returns complete information about a stock in a dictionary format '''
		return ""

	def getStockPrice(self, stockName):
		self.currPrice += random.gauss(0, self.std)
		return self.currPrice


	def _getStockCode(self, stockName):
		return ""


