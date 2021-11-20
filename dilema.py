#!/usr/bin/env python3
from types import MethodType as method
from __init__ import loadStrategies

def align(string: str) -> str:
	return string.replace(': ', ':\t')

class Tournament:
	class Battle:
		def __init__(self, strategy1: method, strategy2: method, duration: int = 30, price: int = 5, cost: int = 1) -> object:
			self.strategy1 = strategy1
			self.strategy2 = strategy2
			self.duration  = duration

			self.name1 = self.strategy1.__name__.replace('_', ' ').replace('strategies.', '').capitalize()
			self.name2 = self.strategy2.__name__.replace('_', ' ').replace('strategies.', '').capitalize()

			self.price = price
			self.cost = cost

			self.string = ''

			self.rank   = {name:0 for name in (self.name1, self.name2)}
			self.memory = (['']  , [''])
			self.turns  = ([True], [True])
			self.game   = {}
		
		def start(self) -> None:
			for day in range(self.duration):
				today1 = self.strategy1.run(self.turns[1], self.memory[0])
				today2 = self.strategy2.run(self.turns[0], self.memory[1])

				self.turns[0].append (today1[0])
				self.turns[1].append (today2[0])
				self.memory[0].append(today1[1])
				self.memory[1].append(today2[1])

				if not self.name1 in self.rank:
					self.rank[self.name1] = 0

				if not self.name2 in self.rank:
					self.rank[self.name2] = 0

				self.rank[self.name1] += (self.price*self.turns[1][-1]) + (self.cost * (not self.turns[0][-1]))
				self.rank[self.name2] += (self.price*self.turns[0][-1]) + (self.cost * (not self.turns[1][-1]))
			self.game = {'turns':{self.name1:self.turns[0], self.name2:self.turns[1]}, 'rank':self.rank}
		
			temp = [f'{name}: {self.rank[name]}' for name in self.rank]
			temp.sort(key = (lambda x: int(x.split(': ')[-1])), reverse = True)
			self.string = strList('\n'.join(temp), 10)
			del temp

	def __init__(self, duration: int = 30, price: int = 5, cost: int = 1) -> object:
		self.duration = duration
		self.strategies = []
		self.rank = {}
		self.game = {}

		self.string = ''

		self.price = price
		self.cost = cost
	
	def getStrategies(self) -> None:
		self.strategies = loadStrategies()

	def new(self) -> None:
		self.getStrategies()

		for strategy1 in self.strategies:
			for strategy2 in self.strategies:
				if strategy1 == strategy2: continue
				battle = Tournament.Battle(strategy1, strategy2, self.duration, self.price, self.cost)
				battle.start()

				if not battle.name1 in self.rank:
					self.rank[battle.name1] = 0

				if not battle.name2 in self.rank:
					self.rank[battle.name2] = 0
				
				self.rank[battle.name1] += battle.rank[battle.name1]
				self.rank[battle.name2] += battle.rank[battle.name2]
				self.game[f'{battle.name1} x {battle.name2}'] = battle.game['turns']
				del battle
	
		temp = [f'{name}: {self.rank[name]}' for name in self.rank]
		temp.sort(key = (lambda x: int(x.split(': ')[-1])), reverse = True)
		self.string = strList('\n'.join(temp), 10)
		del temp
	
	def show() -> None:
		print(self.string)