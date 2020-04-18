from Agent import Agent
from StockMarketTalker import StockMarketTalker
from BSEDataStockMarketTalker import BSEDataStockMarketTalker
from RandomStockMarketTalker import RandomStockMarketTalker
from datetime import datetime
from dateutil.parser import parse

import matplotlib.pyplot as plt
import itertools

import time


class Controller:

	def __init__(self, stockMarketTalker, agentsList):
		self.stockMarketTalker = stockMarketTalker
		self.agentsList = agentsList

		self.plRecList = [0 for agent in agentsList]
		self.buyPrices = [None for agent in agentsList]
		self.quantities = [0 for agent in agentsList]

		self.baseQuantity = 1

		self.agentsRec = [[] for agent in agentsList]


	def run(self, num_episodes=58):

		for i in range(num_episodes):
			for i in range(len(self.agentsList)):
				
				stockName = self.agentsList[i].getStockName()
				stockPrice = self.stockMarketTalker.getStockPrice(stockName)

				print("Stock Price:", stockPrice)

				agentAction = self.agentsList[i].getAction(stockPrice)
				print("Agent Action:", agentAction)
				assert agentAction == "BUY" or agentAction == "HOLD" or agentAction == "SELL"

				currTime = datetime.now()
				currTime = currTime.strftime("%H:%M:%S")
				print("For stock", stockName, "got price", stockPrice, "at time", currTime)

				if agentAction == "BUY":
					print("Bought")
					if self.buyPrices[i] == None:
						self.quantities[i] = self.baseQuantity
						self.buyPrices[i] = stockPrice
					else:
						self.buyPrices[i] = ((self.buyPrices[i] * self.quantities[i]) + stockPrice * self.baseQuantity) / (self.quantities[i] + self.baseQuantity)
						self.quantities[i] += self.baseQuantity

				elif agentAction == "SELL":
					print("Sold")
					profit = self.quantities[i] * (stockPrice - self.buyPrices[i])
					self.plRecList[i] += profit
					self.quantities[i] = 0
					self.buyPrices[i] = None
					print('Agent', self.agentsList[i].getStockName(), 'got a profit of :', profit)

				else: # agentAction == "HOLD"
					pass

				self.agentsRec[i].append((stockPrice, agentAction))
				time.sleep( self.stockMarketTalker.getRequestInterval() )

			print('Total profit is', self.plRecList[i])

	def plot(self, agentNum):
		rec = self.agentsRec[agentNum]
		stockPrices = [stockPrice for (stockPrice, agentAction) in rec]
		actions = [agentAction for (stockPrice, agentAction) in rec]
		actionsDict = {"BUY": "g", "SELL": "r", "HOLD": "b"}
		actions = [actionsDict[act] for act in actions]
		plt.plot(range(len(stockPrices)), stockPrices)
		plt.scatter(range(len(stockPrices)), stockPrices, c=actions)
		plt.legend()
		plt.show()


if __name__ == '__main__':
	#agent = Agent("20 Microns Ltd.")
	agent = []
	agent.append(Agent("Icici Bank Ltd."))
	agent.append(Agent("Shriram Transport Finance Co.ltd."))
	#agent.append(Agent("Jammu & Kashmir Bank Ltd."))

	stockMarketTalker = BSEDataStockMarketTalker()

	controller = Controller(stockMarketTalker, agent)
	controller.run()
	controller.plot(0)