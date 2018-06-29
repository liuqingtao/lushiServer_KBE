# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
from interfaces.cardBase import cardBase
#import d_card_dis
class Avatar(cardBase):
    def __init__(self):
        DEBUG_MSG('Avatar.cell::__init__: [%i]  roleType:[%i]' % (self.id,self.roleType))
        cardBase.__init__(self)
        self.cardID=(20003000+self.roleType)
        cardBase.initProperty(self)
        self.battlefield.AvatarRegiste(self,self.playerID)
        self.cardEntityList = []
        self.cardEntityList.append(self)
        self.createCardEntity((20001000+self.roleType),'SKILL')
        self.createCardListEntities()
        self.battlefield.AvatarRegiste(self,self.playerID)

    def createCardEntity(self, cardID, pos='KZ'):
        DEBUG_MSG('Avatar.cell::createCardEntity__init__: [%i] cardID[%i]  pos:[%s]' % (
            self.id, cardID, pos))
        params = {
            'cardID': cardID,
            'pos': pos,
            "battlefiled": self.battlefiled,
            'avatar': self,
            'playerID': self.playerID
        }
        e=KBEngine.createEntity('card',self.spaceID,tuple(self.position),tuple(self.direction),params)
        self.cardEntityList.append(e)
    
    def createCardListEntities(self):
        for cardID in self.cardList:
            self.createCardEntity(cardID)
