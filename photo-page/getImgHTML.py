# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:26:52 2020

@author: alexw
"""

import os

out = '<div class="col-sm-12 col-md-4">\n<a class="lightbox" href="img/1.jpg">\n<img src="img/1.jpg" alt="1">\n</a>\n</div>\n'
for n in range(2, 139):
    base = '<div class="col-sm-12 col-md-4">\n<a class="lightbox" href="img/{}.jpg">\n<img src="img/{}.jpg" alt="{}">\n</a>\n</div>\n'.format(n,n,n)
    out += base
    
with open('img-html.txt', 'w') as f:
    f.write(out)