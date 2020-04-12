# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:19:35 2020

@author: alexw
"""

import os
print(os.getcwd())
n = 1
for file in os.listdir(os.getcwd()):
    if not file.endswith(".py"):
        os.rename(file, str(n) + ".jpg")
        n += 1