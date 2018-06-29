# -*- coding: utf-8 -*-
import KBEngine
import d_card_dis
import random
import re
from KBEDebug import *
from array import *


class BattleField(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        DEBUG_MSG("BattleField.cell[%i].init" %(self.id))
        self.player0=None
        self.player1=None

    def AvatarRegiste(self,avatarEntity,playerID):
        DEBUG_MSG("BattleField.cell[%i].AvatarRegiste entityID:[%s]" %(self.id,avatarEntity.id))
        if(playerID==1):
            self.player1=avatarEntity
        else:
            self.player0=avatarEntity
        if(self.player0!=None and self.player1!=None):
            self.players={
                self.player0,
                self.player1
            }
        self.startBattle()
    def startBattle(self):
        DEBUG_MSG("BattleField.cell[%i].startBattle" %(self.id))
    def getAllEntity(self):
        return self.player0.cardEntityList+self.player1.cardEntityList