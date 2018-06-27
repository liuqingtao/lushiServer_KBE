# -*- coding: utf-8 -*-
import random
from KBEDebug import *
from interfaces.cardBase import cardBase

import d_card_dis

class Avatar(cardBase):
    def __init__(self):
        DEBUG_MSG('Avatar.cell::__init__: [%i]  roleType:[%i]' % (self.id,self.roleType))