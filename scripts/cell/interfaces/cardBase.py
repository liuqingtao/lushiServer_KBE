# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import d_card_dis
import random
import copy
#from interfaces.spell import spell
#from interfaces.Buff import Buff

#class cardBase(KBEngine.Entity,spell):
class cardBase(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		'''
		self.pos
		HAND		手牌
		KZ			卡组中
		0-6			场上1-7号
		HERO		英雄
		WEAPON		武器
		SKILL		技能
		DEAD		死过的卡（随从）
		USED		用过的卡（法术）
		SECRRET		奥秘
		BUFF        BUFF环境buff分发牌
		'''
		if self.cardID !=0:
			self.initProperty()
	def initProperty(self):
		cardID = self.cardID
		self.cost = d_card_dis.datas[cardID]["cost"]
		self.att = d_card_dis.datas[cardID]["att"]
		self.HP = d_card_dis.datas[cardID]["HP"]
		self.maxHP = d_card_dis.datas[cardID]["HP"]
		effectBool = d_card_dis.datas[cardID]["effectBool"]
		self.isTaunt = int( effectBool[0:1])
		self.isRush = int(effectBool[1:2])
		self.isWindfury = int( effectBool[2:3])
		self.isDivineShield = int( effectBool[3:4])
		self.isAbledForever = int(effectBool[4:5])
		if self.isAbled == 0:
			self.isAbled = int(effectBool[1:2])
		self.isStealth = int( effectBool[5:6])
		self.frozen = 0
		self.immune = 0
		self.race = d_card_dis.datas[cardID].get('race','')
		self.envBuff = d_card_dis.datas[cardID].get('envBuff',0)

		self.attSum = 0
		self.type = d_card_dis.datas[cardID]["type"]
		self.poison = d_card_dis.datas[cardID]["poison"]
		self.suckBlood = d_card_dis.datas[cardID]["suckBlood"]

		self.buffList = []
		self.sendBuffList = []

		self.chooseDataStore = {
			'targetID': 0,
			'needPos': 0,
			'active': False
		}
		DEBUG_MSG('card.cell::__init__: [%i]  cardID:[%s]' % (self.id,self.cardID))
	def changePos(self,pos):
		DEBUG_MSG('card.cell::changePos: [%i]  pos:[%s]' % (self.id,pos))
		self.pos=pos
	def  reqUse(self,callerID,targetID):
		DEBUG_MSG('card.cell::reqUse: [%i] targetID[%s]' % (self.id,targetID))

	def reqAtt(self,callerID,targetID)
		DEBUG_MSG('card.cell::reqAtt: [%i] targetID[%s]' % (self.id,targetID))














