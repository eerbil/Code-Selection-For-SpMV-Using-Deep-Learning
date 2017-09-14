import numpy as np
import scipy.io as sio
import math
import subprocess
np.set_printoptions(threshold='nan')
from PIL import Image

matrices = open("matrices_square.txt", 'r')
for line in matrices:
    name = line.rstrip().split(' ')
    #directory = "mcca.mtx"
    directory = "/home/matrices/mtx/" + name[0] + "/" + name[1] + "/" + name[1] + ".mtx"
    mtx = sio.mmread(directory)
    mtx_row = sio.mminfo(directory)[0]
    mtx_col = sio.mminfo(directory)[1]
    print name[1]

    if mtx_row <= 1000:
        coef = 1
    elif 1000 < mtx_row <= 5000:
        coef = 5
    elif 5000 < mtx_row <= 10000:
        coef = 10
    elif 10000 < mtx_row <= 50000:
        coef = 50
    elif 50000 < mtx_row <= 100000:
        coef = 100
    elif 100000 < mtx_row <= 500000:
        coef = 500
    elif 500000 < mtx_row <= 1000000:
        coef = 1000
    elif 1000000 < mtx_row <= 5000000:
        coef = 5000
    else:
        coef = 10000
    
#    print coef
    if (mtx_row % coef) != 0:
        img_row = mtx_row + (coef - (mtx_row % coef))
    else:
        img_row = mtx_row
#    print img_row
    
    row_cnt = 0
    col_cnt = 0
#    print mtx
    mtx_int = np.zeros((img_row / coef, img_row / coef))
    for i in range(len(mtx.col)):
#        print math.ceil((mtx.row[i]+1)/coef)-1
        mtx_int[int(math.ceil((mtx.row[i]+1)/coef)-1)][int(math.ceil((mtx.col[i]+1)/coef)-1)] += 1
#    print mtx_int
    
    im = Image.new("RGB", (img_row / coef, img_row / coef))
    pix = im.load()
    for i in range(img_row / coef):
        for j in range(img_row / coef):
            # print (int(255*mtx_int[i][j]), int(255*mtx_int[i][j]), int(255*mtx_int[i][j]))
            pix[(i, j)] = (int(255 * mtx_int[i][j]), int(255 * mtx_int[i][j]), int(255 * mtx_int[i][j]))
    inverted = Image.eval(im, lambda (x): 255 - x)
    inverted.save(name[1] + ".png", "PNG")
e = 'echo "Test completed on milner" | ssmtp eerbil13@ku.edu.tr'
subprocess.call(e, shell=True)
