# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
from interfaces.cardBase import cardBase
import d_card_dis
class Avatar(cardBase):
    def __init__(self):
        DEBUG_MSG('Avatar.cell::__init__: [%i]  roleType:[%i]' % (self.id,self.roleType))
        cardBase.__init__(self)
        self.cardID=(20003000+self.roleType)
        cardBase.initProperty(self)
        self.pos="HERO"
        self.avatar=self
        self.cardEntityList = []
        self.followerList=[]
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

    def reqGiveUp(self,callerID):
        DEBUG_MSG('Avatar.cell::reqGiveUp: [%i] ' % (self.id))
        self.battlefield.reqGiveUp(self.playerID)
    def battleEnd(self,success):
        DEBUG_MSG('Avatar.cell::battleEnd: [%i]  success:[%s]' % (self.id,success))
        self.base.battleEnd(success)
    def getCard(self,cardID):
        DEBUG_MSG('Avatar.cell::getCard: [%i] cardID[%s]' % (self.id,cardID))
        self.createCardEntity(cardID,'HAND')
    def getCardFromKz(self,cardSum=1):
        kzCards=self.getCardByPos('KZ')
        DEBUG_MSG('Avatar.cell::getCardFromKz: [%i] kzCards[%s] cardSum[%s]' % (self.id,kzCards,cardSum))
        chouCards=random.sample(kzCards,cardSum)
        for card in chouCards:
            card.changePos('HAND')
    
    def useCrystal(self.crystalSum):
        DEBUG_MSG('Avatar.cell::useCrystal: [%i] crystalSum[%s] ' % (self.id,crystalSum))
        if  self.CrystalAvaliable<crystalSum:
            return False
        self.CrystalAvaliable-=crystalSum
        return True

    def followerPosAssigned(self,entity):
        DEBUG_MSG('Avatar.cell::followerPosAssigned: [%i] entityID[%i] ' % (self.id,entity.id))
        if len(self.followerList)>6:
            return
        self.followerList.append(entity)
        self.followerPosUpdate()

    def followerPosUpdate(self):
        for i in range(len(self.followerList)):
            self.followerList[i].changePos(str(i))
    def getCardByPos(self,pos):
        cards=[]
        DEBUG_MSG("self.cardEntityList[%i].count:[%i]" % (self.id,len(self.cardEntityList)))
        for card in self.cardEntityList:
            if card.pos==pos:
                cards.append(card)
        return cards