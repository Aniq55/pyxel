from PIL import Image
import cv2
from keygen import *
import numpy
import argparse
import getpass
import time
#
# def automate_swap(arr, a, b):
#     L = len(a)
#     for i in range(L):
#         temp = arr[a[i][0], a[i][1]]
#         arr[a[i][0], a[i][1]] = arr[b[i][0], b[i][1]]
#         arr[b[i][0], b[i][1]] = temp
#

def encode(image_path, pwd, init_tuple=None):
    extension=image_path.split('.')[-1]

    arr = cv2.imread(image_path)
    (W, H) = im.size
    print(W, H)
    TUPLE = key_init(pwd, W, H)
    if init_tuple!=None:
        TUPLE = init_tuple
    degree= int(3.5*W*H)

    a= TUPLE
    b= TUPLE

    # degree =20
    for j in range(degree):
        a=b
        b= next_tuple(a)
        L = len(a)
        for i in range(L):
            a1, a2 = a[i][0]%H, a[i][1]%W
            b1, b2 = b[i][0]%H, b[i][1]%W
            temp = arr[a1, a2]
            # print(a1,a2,b1,b2)
            arr[a1, a2] = arr[b1, b2]
            arr[b1, b2] = temp

    tokenized= image_path.split('.')
    saved_path= tokenized[0]+'_enc.'+tokenized[1]

    cv2.imwrite(saved_path, arr)
    return TUPLE


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='absolute/relative path to the image file')
    args = parser.parse_args()

    image_path = args.path

    if(image_path is None):
        print ('Please provide the path to image file. Try again.')
        exit(0)
    pwd = getpass.getpass("Enter password: ")
    seed= encode(image_path, pwd)
