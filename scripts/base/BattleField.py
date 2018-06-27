# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
class BattleField(KBEngine.Base):
    def __init__(self):
        DEBUG_MSG("BattleField[%s] init"% self.id)
        KBEngine.Base.__init__(self)
        self.createInNewSpace(None)

    def onTimer(self,id,userArg):
        """
        KBEngine method.
        使用addTimer后，当时间到达则该接口被调用
        @param id : addTimer的返回值ID
        @param userArg ： addTimer最后一个参数所给入的数据
        """
    
    def onGetCell(self):
        DEBUG_MSG("cell has been created")
        self.player0.marchSuccess(self.cell)
        self.player1.marchSuccess(self.cell)
