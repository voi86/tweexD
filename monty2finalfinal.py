# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:53:49 2019

@author: tweeb
"""

# Thuy Le - MHI 289I - Homework 2 - Part 1

import random

def montyalways():
    if select == prize:
        return False
    else:
        return True

def montynever():
    if select == prize:
        return True
    else:
        return False
    
prize = random.randint(1,3)
select = random.randint(1,3)

montyalways()
montynever()