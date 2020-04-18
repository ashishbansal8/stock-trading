''' 
	Created on 20th March by Vaibhav

	Purpose:- This file is an implementation class for StockMarketTalker.
			  It uses bsedata module to get information from stock market
'''

from bsedata.bse import BSE
import time

from StockMarketTalker import StockMarketTalker


class BSEDataStockMarketTalker(StockMarketTalker):


	def __init__(self):
		super(BSEDataStockMarketTalker, self).__init__()
		self.bse = BSE()
		self.companyCodesToCompanyNamesMap = self.bse.getScripCodes()
		assert(len(self.companyCodesToCompanyNamesMap) != 0)
		self.companyNamesToCompanyCodesMap = {value: key for key, value in self.companyCodesToCompanyNamesMap.items()}
		self.lastRequestTimestamp = 0
		self.MIN_TIME_BW_REQUESTS = 60	# So that we don't get banned by servers of BSE

	def getRequestInterval(self):
		return self.MIN_TIME_BW_REQUESTS


	def getStockInfo(self, stockName):
		''' Returns complete information about a stock in a dictionary format '''
		assert time.time() - self.lastRequestTimestamp > self.MIN_TIME_BW_REQUESTS, 'Please wait for {} seconds between subsequent server requests'.format(self.MIN_TIME_BW_REQUESTS)
		self.lastRequestTimestamp = time.time()
		stockCode = self._getStockCode(stockName)
		return self.bse.getQuote(stockCode)

	def getStockPrice(self, stockName):
		try:
			stockInfo = self.getStockInfo(stockName)
		except:
			stockInfo = self.getStockInfo(stockName)

		return float(stockInfo['currentValue'])


	def _getStockCode(self, stockName):
		if stockName in self.companyCodesToCompanyNamesMap:
			return stockName
		assert stockName in self.companyNamesToCompanyCodesMap, 'Must supply either a valid company name or company code'
		return self.companyNamesToCompanyCodesMap[stockName]


