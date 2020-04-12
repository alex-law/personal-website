import tinify
import os
tinify.key = 'y08PDYFGvc5MNsrKDrMKZYgMHFlDCVp7'

for c, src in enumerate(os.listdir(os.getcwd())):
    if src.endswith('.jpg'):
        dst = '{}.jpg'.format(str(c))
        compressed = tinify.from_file(src)
        compressed.to_file(dst)
        