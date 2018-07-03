# -*- coding: utf-8 -*-
import KBEngine
import random
import time
from KBEDebug import *

class Avatar(KBEngine.Proxy):
	"""
	角色实体
	"""
	def __init__(self):
		KBEngine.Proxy.__init__(self)

		DEBUG_MSG('Avatar.base::__init__: [%i]' % self.id)

		self.cellData['position'] = [0,0,0]
		self.bf = self.cellData['battlefield']
		self.cellData['playerID']=self.playerIDB
		self.createCellEntity(self.bf)
	def onGetClient(self):
		DEBUG_MSG('Avatar.base:onGetClient:[%i].'% self.id)
	

	def battleEnd(self,success):
		DEBUG_MSG('Avatar.base::battleEnd: [%i]  success:[%s]' % (self.id,success))
		self.client.battleEnd(success)
		self.giveClientTo(self.account)

		



	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		if 1 == userArg:
			self.onDestroyTimer()

	def onGetCell(self):
		"""
		KBEngine method.
		entity的cell部分实体被创建成功
		"""
		DEBUG_MSG('Avatar::onGetCell: %s' % self.cell)


		
	def onClientDeath(self):
		"""
		KBEngine method.
		entity丢失了客户端实体
		"""
		DEBUG_MSG("Avatar[%i].onClientDeath:" % self.id)
		# 防止正在请求创建cell的同时客户端断开了， 我们延时一段时间来执行销毁cell直到销毁base
		# 这段时间内客户端短连接登录则会激活entity
		#self._destroyTimer = self.addTimer(1, 1, 1)
		#self.account.onClientDeath()
			
	def onClientGetCell(self):
		"""
		KBEngine method.
		客户端已经获得了cell部分实体的相关数据
		"""
		DEBUG_MSG("Avatar[%i].onClientGetCell:%s" % (self.id, self.client))
		self.avatarRegiste()

	def onDestroyTimer(self):
		DEBUG_MSG("Avatar(BASE)::onDestroyTimer: %i" % (self.id))
		self.destroy()



