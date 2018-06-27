# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
class Hall(KBEngine.Base):
    def __init__(self):
        DEBUG_MSG("Hall init")
        KBEngine.Base.__init__(self)

        #储存大厅
        KBEngine.globalData["Halls"]=self

        #存放所有正在匹配玩家mailBox
        self.OnMarchingPlayer=[]

        self.addTimer(6,3,1)
    def reqAddMarcher(self,player):
        #此函数添加匹配玩家入列表
        DEBUG_MSG("Account[%i].reqAddMarcher:"% player.id)
        if player in  self.OnMarchingPlayer:
            return
        self.OnMarchingPlayer.append(player)
    def reqDelMarcher(self,player):
        #此函数删除匹配玩家从列表
        DEBUG.DEBUG_MSG("Hall[%s].reqDelMarcher:" % player.id)
        if player not in self.OnMarchingPlayer:
            return
        self.OnMarchingPlayer.remove(player)
    def march(self):
        DEBUG_MSG("Hall.march:marchersSum:[%s]" % len(self.OnMarchingPlayer))
        if(len(self.OnMarchingPlayer)>1):
            players=[self.OnMarchingPlayer[0],self,OnMarchingPlayer[1]]
            self.marchSuccess(players)
            del self.OnMarchingPlayer[0]
            del self.OnMarchingPlayer[1]
    def marchSuccess(self,players):
        DEBUG.DEBUG_MSG("Hall.marchSuccess:playerIDs[%s]" % players)
        prarm={
            "player0":players[0]
            "player1":players[1]
        }
        BattleField=KBEngine.createBaseAnywhere("BattleField",prarm)    
    def onTimer(self,id,userArg):
        """
        KBEngine method.
        使用addTimer后，当时间到达则该接口被调用
        @param id : addTimer的返回值ID
        @param userArg ： addTimer最后一个参数所给入的数据
        """
        if userArg==1:
            self.march()