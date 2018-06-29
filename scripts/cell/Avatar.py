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
        DEBUG_MSG('Avatar.cell::createCardEntity: [%i] cardID[%i]  pos:[%s]' % (
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
    def setSituation(self,situation):
        DEBUG_MSG('Avatar.cell::setSituation: [%i] situation[%s]' % (self.id,situation))
        self.situation=situation
        if  situation==1:
            self.newRound()        
    def newRound(self):
        DEBUG_MSG('Avatar.cell::newRound: [%i] ' % (self.id))
        self.getCardFromKz(1)        

    def reqEndRound(self):
        DEBUG_MSG('Avatar.cell::reqEndRound: [%i] ' % (self.id))
        if self.situation==1:
            self.battlefield.endRound()
    def getCard(self,cardID):
        DEBUG_MSG('Avatar.cell::getCard: [%i] cardID[%s]' % (self.id,cardID))
        self.createCardEntity(cardID,'HAND')
    def getCardFromKz(slef,cardSum=1):
        DEBUG_MSG('Avatar.cell::getCardFromKz: [%i] cardSum[%s]' % (self.id,cardSum))
        kzCards=self.getCardByPos('KZ')
        chouCards=random.sample(kzCards,cardSum)
        for card in chouCards:
            card.changePos('HAND')
    def getCardByPos(self,pos):
        cards=[]
        for card in self.cardEntityList:
            if card.pos=pos:
                cards.append(card)
        return cards