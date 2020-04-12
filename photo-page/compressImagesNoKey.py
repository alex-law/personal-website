"""Run in photo folder to compress images using tinify"""

import tinify
import os
tinify.key = '#'

for c, src in enumerate(os.listdir(os.getcwd())):
    if src.endswith('.jpg'):
        dst = '{}.jpg'.format(str(c))
        compressed = tinify.from_file(src)
        compressed.to_file(dst)
        