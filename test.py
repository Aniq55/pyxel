import cv2
import numpy as np

#Mean Square Error
global file_name, file_name2


file_name= 'testimg/cat_enc_dec.png'
file_name2= 'testimg/cat_enc.png'

def mse():
	im1 = cv2.imread(file_name,0)
	im2 = cv2.imread(file_name2,0)
	H, W = im1.shape
	MSE  = 0.0
	for i in range (H):
		for j in range(W):
			MSE = MSE + np.square(im1[i][j] - im2[i][j])
	MSE = MSE/(H*W)
	return MSE

#peak signal to noise ratio	
def psnr():
	MSE = mse()
	PSNR = 10*np.log(255*255/MSE)
	return PSNR
	
#entropy analysis	
def ent():
	counter = np.zeros(255)
	counter2 = np.zeros(255)
	im1 = cv2.imread(file_name,0)
	im2 = cv2.imread(file_name2,0)
	H, W = im1.shape
	for i in range (H):
		for j in range(W):
			counter[im1[i][j]-1] = counter[im1[i][j]-1]+1	
	H_m = 0.0
	for i in range (len(counter)):
		p_i = counter[i]/(H*W)
		H_m= H_m - p_i*np.log(p_i+1)/3.321928
	for i in range (H):
		for j in range(W):
			counter2[im2[i][j]-1] = counter2[im2[i][j]-1]+1	
	H_m2 = 0.0
	for i in range (len(counter)):
		p_i = counter2[i]/(H*W)
		H_m2= H_m2 - p_i*np.log(p_i+1)/3.321928
		
	return (H_m,H_m2)
	
#Difference Attack Test
def npcr():
	counter = 0
	im1 = cv2.imread(file_name,0)
	im2 = cv2.imread(file_name2,0)
	H, W = im1.shape
	for i in range (H):
		for j in range(W):
			if im1[i][j] == im2[i][j]:
				counter = counter+1
	NPCR	= 1.0*counter/(1.0*H*W)
	return NPCR
	
def uaci():
	im1 = cv2.imread(file_name,0)
	im2 = cv2.imread(file_name2,0)
	H, W = im1.shape
	UACI  = 0.0
	for i in range (H):
		for j in range(W):
			UACI = UACI + (im1[i][j] - im2[i][j])
	UACI = UACI/(255*H*W)
	return UACI
	
print(mse())
print(psnr())
print(ent())
print(npcr())
print(uaci())
				
	

		
		
				
	
	
			
	
