# python
# import dice
# saicoro = dice.Dice()
# saicoro.face   初期化メソッド6
# saicoro.shoot()    ランダムに１から６の数字が出る

import random

class Dice():
	face = 6
	def __init__(self,val=6):
		self.face = val

	def shoot(self):
		return random.randint(1,self.face)