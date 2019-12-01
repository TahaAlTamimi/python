#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:29:52 2019

@author: owner
"""
import statistics as st
import math
from PIL import Image
import  doctest
import random



#Q1=============================================================================
# x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
# print(st.mean(x))
# print(st.harmonic_mean(x))
# print(st.median(x))
# print(st.median_low(x))
# print(st.median_high(x))
# print(st.median_grouped(x))
# print(st.mode(x))
# print(st.pstdev(x))
# print(st.pvariance(x))
# print(st.stdev(x))
# print(st.variance(x))
# =============================================================================

# Q2=============================================================================
# print( random.random() )
# print ( random.randrange(100) )
# print ( random.choice(['Ali', 'Khalid', 'Hussam']) )
# print ( random.sample(range(1000), 10) )
# print ( random.choice('Orange Academy'))
# items = [1,5,8,9,2,4]
# random.shuffle(items)
# print( items )
# print ( random.randint(20,30) )
# print ( random.randrange(1000, 2111, 5) )
# print ( random.uniform(10000, 11000))
# print()
# =============================================================================


#Q3 =============================================================================
# print ('pi:',math.pi)
# print(math.cos(200))
# print(math.sin(30))
# print(math.tan(180))
# print(math.floor(10.8))
# print(math.ceil(10.8))
# 
# =============================================================================

from PIL import Image,ImageFilter,ImageDraw
im1=Image.open("cats.jpg")
im2=Image.open("cats.jpg").resize(im1.size)
im1.show()
print (im1.format , im1.size , im1.mode)
im1_filp=im1.transpose(Image.FLIP_TOP_BOTTOM)
im1_filp.show()
greyscale_image=im1.convert('L')
greyscale_image.show()
croppedImage=im1.crop((0,0,50,50))
croppedImage.show()
draw=ImageDraw.Draw(im1)
draw.line((0,0)+im1.size, fill = (225,225,225))
draw.line((0,im1.size[1], im1.size[0],0),fill=(225,225,225))
draw.text((im1.size[0]/2-im1.size[0]/2,im1.size[1]/2+20),'Tamimi',fill=(225,225,0))
draw.text((im1.size[0]/2-im1.size[0]/2,im1.size[1]/2-60),'Image',fill=(225,225,0))
im1.show()
newImage2=im2.filter(ImageFilter.SHARPEN)
newImage2.show()
newImage2=im2.filter(ImageFilter.EDGE_ENHANCE)
newImage2.show()
newImage3=im2.filter(ImageFilter.FIND_EDGES)
newImage3.show()
newImage4=im2.filter(ImageFilter.SMOOTH)
newImage4.show()
Image.blend(im1,im2,0.5).save('newphoto.jpg'.format(0.5))
im=Image.open('newphoto.jpg')
im.show()
blurred=im1.filter(ImageFilter.BLUR)
im1.show()
size=(128,128)
saved="timon4.png"
try:im
except:print("Unable to load image")
im.thumbnail(size)
im.save(saved)
im.show()
im1_flip=im1.transpose(Image.ROTATE_90)
im1_flip.show()
mask=Image.open('mask.jpg')
mask=mask.resize(im1.size)
Image.composite(im1,im2,mask).save('maskimage.jpg')
imagMask=Image.open('maskimage.jpg')
imagMask.show()













# =============================================================================
# x=[3,1.5,4.5,6.75,2.25,5.75,2.25]
# print(st.mean(x))
# print(st.harmonic_mean(x))
# print(st.median(x))
# print(st.median_low(x))
# print(st.median_high(x))
# print(st.median_grouped(x))
# print(st.mode(x))
# print(st.pstdev(x))
# print(st.pvariance(x))
# print(st.stdev(x))
# print(st.variance(x))
# 
# 
# =============================================================================

# =============================================================================
# print( random.random() )
# print ( random.randrange(0, 101, 2) )
# =============================================================================

# =============================================================================
# print( random.random() )
# print ( random.randrange(100) )
# print ( random.choice(['Jordan', 'USA', 'UK']) )
# print ( random.sample(range(100), 5) )
# print ( random.choice('abcdefghij') )
# items = [11, 12, 30, 14, 35, 66, 17]
# random.shuffle(items)
# print( items )
# print ( random.randint(10, 20) )
# print ( random.randrange(0, 101, 2) )
# print ( random.uniform(1, 100))
# print()
# =============================================================================

# =============================================================================
# print ('pi: %.40f' % math.pi)
# n = 100.1
# print(math.floor(n))
# print(math.ceil(n))
# =============================================================================


# =============================================================================
# 
# def sum(a,b):
# 
#     """
#     Calculates the sum of a and b 
#     >>> sum(1,1)
#     2
#     >>> sum(1,-1)
#     0
#     >>> sum(-1,-1)
#     -2
#     >>> sum(0,-10)
#     -10
#     >>>
#     
#     """
#     return a+b    
#     
# if __name__=="__main__":
#     doctest.testmod(verbose=True)
# =============================================================================
# =============================================================================
# from PIL import Image
# im=Image.open("cats.jpg") 
# print(im.format,im.size,im.mode)
# im.show()
# =============================================================================
    
    
# =============================================================================
# from PIL import Image,ImageFilter
# im=Image.open("cats.jpg") 
# blurred=im.filter(ImageFilter.BLUR)
# # =============================================================================
# # print(im.format,im.size,im.mode)
# # =============================================================================
# 
# im.show()
# blurred.show()
# blurred.save('catsblurred.png')    
#     
# =============================================================================
# =============================================================================
# from PIL import Image  
# size=(128,128)
# saved='cats.jpg'
# try:
#     im=Image.open("cats.jpg") 
# except:
#     print('unable')
#     
# im.thumbnail(size)
# im.save(saved)
# im.show()
#     
# =============================================================================
# =============================================================================
# from PIL import Image  
# 
# im=Image.open("cats.jpg")    
# greyimage=im.convert('L')
# greyimage.show()
# greyimage.save('savegrey.png')
#     
#     
# =============================================================================

# =============================================================================
# from PIL import Image,ImageFilter
# im=Image.open("imim.jpeg") 
# blurred=im.filter(ImageFilter.SMOOTH)
# # # =============================================================================
# # # print(im.format,im.size,im.mode)
# # # =============================================================================
# # 
# im.show()
# blurred.show()
# blurred.save('imimblurred5.png') 
# =============================================================================

# =============================================================================
# from PIL import ImageDraw
# im=Image.open("imim.jpeg") 
# im=im.resize((500,500)) 
# im.show()
# =============================================================================













































    
    
    
    
    
    