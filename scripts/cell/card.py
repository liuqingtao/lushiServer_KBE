# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
from interfaces.cardBase import cardBase
#import d_card_dis


class card(cardBase):
    def __init__(self):
        DEBUG_MSG('Avatar.cell::card__init__: [%i]' % (
            self.id))
        cardBase.__init__(self)
        

    