import cv2
import numpy as np
from skimage import data, img_as_float
from skimage.measure import compare_ssim as ssim

# Calculation of structural similarity index
# Needs automation for acquiring results for analysis
def similarity_index(image1, image2):
    im1 = cv2.imread(image1, 0)
    im2 = cv2.imread(image2, 0)
    # f1 = np.fft.fft2(im1)
    # f2 = np.fft.fft2(im2)
    # print(f2)
    # print(f1)
    ssim_im = ssim(im1, im2, data_range=im2.max() - im2.min())
    # c= np.corrcoef(f1,f2)
    print(ssim_im)

similarity_index('emma.png', 'emma_enc.png')
