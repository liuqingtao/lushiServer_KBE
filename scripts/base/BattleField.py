# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
class BattleField(KBEngine.Base):
    def __init__(self):
        DEBUG_MSG("BattleField[%s] init"% self.id)
        KBEngine.Base.__init__(self)
        self.player0.marchSuccess(self)
        self.player1.marchSuccess(self)

    def onTimer(self,id,userArg):
        """
        KBEngine method.
        使用addTimer后，当时间到达则该接口被调用
        @param id : addTimer的返回值ID
        @param userArg ： addTimer最后一个参数所给入的数据
        """