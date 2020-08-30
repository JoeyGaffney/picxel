from PIL import Image
import numpy as np
from matplotlib import pyplot
from matplotlib import image
import random
###################################################
## Import Image here
image = Image.open('src/pics/lit.jpg')
## Set the Size here
size = 128 #px
###################################################
load_img_rz = np.array(image.resize((size,size)))
Image.fromarray(np.uint8(load_img_rz)).save('r_pic.jpg')
grey_img = np.zeros(shape = (size,size))
threshold = 300
bl_threshold = 150
wh_threshold = 500
for i in range(0,size):
    for j in range(0,size):
        if(sum(load_img_rz[i,j]) < bl_threshold):
            grey_img[i,j] = 0
            if(j<size-1 and random.randint(1,16) == 2):
                grey_img[i,j+1] = 0
            if(i<size-1 and random.randint(1,16) == 2):
                grey_img[i+1,j] = 0
            if(j > 0 and random.randint(1,16) == 2):
                grey_img[i,j-1] = 0
        elif(sum(load_img_rz[i,j]) > wh_threshold):
            grey_img[i,j] = 255
            if(j<size-1 and random.randint(1,2) == 2):
                grey_img[i,j+1] = 255
            if(i<size-1 and random.randint(1,2) == 2):
                grey_img[i+1,j] = 255
            if(j>0 and random.randint(1,2) == 2):
                grey_img[i,j-1] = 255
        elif(sum(load_img_rz[i,j]) < threshold and grey_img[i,j] != 255):
            grey_img[i,j] = 0
            if(j < size-1 and random.randint(1,4) == 2):
                grey_img[i,j+1] = 255
            if(i < size-1 and random.randint(1,4) == 2):
                grey_img[i+1,j] = 255
                if(j < size-1 and random.randint(1,4) == 2):
                    grey_img[i+1,j+1] = 255
                if(j > 0 and random.randint(1,4) == 2):
                    grey_img[i+1,j-1] = 255
        elif(sum(load_img_rz[i,j]) >= threshold):
            grey_img[i,j] = 255
        
Image.fromarray(np.uint8(grey_img)).save('bw_pic.jpg')