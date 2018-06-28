# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import random

class Account(KBEngine.Proxy):
	def __init__(self):
		self.Gold=99999
		self.Kabao=10
		if(len(self.AvatarList)==0):
			self.randomInitKZ()
		KBEngine.Proxy.__init__(self)
		while len(self.CardList)<50:
			self.CardList.append(random.randint(10000001,10000000+50))
		self.CardList=self.CardList
		self.chooseAvatarStore=-1 
	def randomInitKZ(self):
		ls = []
		for i in range(30):
			ls.append(random.randint(10000001,10000000+50))
		roleType = 0
		name = "随机生成卡组"
		index = -1
		self.reqChangeAvatar(roleType,ls,name,index)	
	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
		
	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("account[%i] entities enable. mailbox:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()
	def reqChangeName(self,name):
		DEBUG_MSG("Account[%i].reqChangeName:[%s]" % (self.id,name))
		if name=="":
			return
		self.Name=name	
	def reqBuyKabao(self,kabaoSum):
		DEBUG_MSG("Account[%i].reqBuyKabao:[%s]" % (self.id,kabaoSum))
		if self.Gold<kabaoSum*100:
			return
		self.Gold-=kabaoSum*100
		self.Kabao+=kabaoSum
	def reqOpenKabao(self):
		DEBUG_MSG("Account[%i].reqOpenKabao:" % (self.id))
		if self.Kabao<1:
			return
		self.Kabao-=1
		ls=[]
		for i in range(5):
			f=random.randint(10000001,10000051)
			ls.append(f)
			self.CardList.append(f)
		self.CardList=self.CardList
		self.client.onOpenPack(ls)
	def reqChangeAvatar(self,roleType,cardList,name,index):
		DEBUG_MSG("Account[%i].reqChangeAvatar:roleType[%s]  index[%s] cardlist[%s] name:[%s]" % (self.id,roleType,index,cardList,name))
		dic={
			'roleType':roleType,
			'name':name,
			'cardList':cardList,
		}
		if index==-1:
			self.AvatarList.append(dic)
		else:
			if index > len(self.AvatarList)-1:
				self.AvatarList.append(dic)
			else:
				self.AvatarList[index]=dic
		self.AvatarList=self.AvatarList

	def reqDelAvatar(self,index):
		DEBUG_MSG("Account[%i].reqDelAvatar:index[%s]" % (self.id,index))
		if index > len(self.AvatarList)-1:
			DEBUG_MSG("Account[%i].reqDelAvatar:index[%s] fail" % (self.id,index))
			return
		del self.AvatarList[index]
		self.AvatarList=self.AvatarList
	def reqStartMarch(self,avatarIndex):
		DEBUG_MSG("Account[%i].reqStartMarch:avatarIndex:[%s]" % (self.id,avatarIndex))
		KBEngine.globalData["Halls"].reqAddMarcher(self)
		self.chooseAvatarStore=avatarIndex
	def reqStopMarch(self):
		DEBUG_MSG("Account[%i].reqStopMarch" % (self.id))
		KBEngine.globalData["Halls"].reqDelMarcher(self)
	def marchSuccess(self,battlefieldCell):
		DEBUG_MSG("Account[%i].battleFieldBase[%s]" % (self.id,battlefieldCell.id))

		dic={
			'roleType':self.AvatarList[self.chooseAvatarStore]['roleType'],
			'battlefield':battlefieldCell,
			'cardList':self.AvatarList[self.chooseAvatarStore]['cardList'],
			'account':self,
			'nameA':self.Name,
		}
		self.client.enterBattlefield()
		self.Avatar=KBEngine.createBaseAnywhere("Avatar",dic)

	def reqEnterBattlefield():
		DEBUG_MSG("Account[%i].reqEnterBattlefield" % (self.id))
		self.giveClientTo(self.Avatar)
		self.Avatar.onGetClient()
	