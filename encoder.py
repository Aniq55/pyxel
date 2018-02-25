from PIL import Image
from keygen import *
import numpy
# from utils import *
import argparse
import getpass


#
# def automate_swap(arr, a, b):
#     L = len(a)
#     for i in range(L):
#         temp = arr[a[i][0], a[i][1]]
#         arr[a[i][0], a[i][1]] = arr[b[i][0], b[i][1]]
#         arr[b[i][0], b[i][1]] = temp
#

def encode(image_path, pwd):
    extension=image_path.split('.')[-1]
    try:
        im = Image.open(image_path, "r")
    except FileNotFoundError:
        print ('Image path is incorrect. Try again.')
        exit(0)

    im = Image.open(image_path, "r")
    # arr = im.load()  # pixel data stored in this 2D array
    arr = numpy.array(im)
    (W, H) = im.size
    print(W, H)
    TUPLE = key_init(pwd, W, H)
    degree= int(0.36*W*H)

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
            print(a1,a2,b1,b2)
            arr[a1, a2] = arr[b1, b2]
            arr[b1, b2] = temp

    tokenized= image_path.split('.')
    saved_path= tokenized[0]+'_enc.'+tokenized[1]
    # im.show() #To display the image im
    output= Image.fromarray(arr, mode='RGB')
    output.save(saved_path)
    # return (im,arr,saved_path)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='absolute/relative path to the image file')
    args = parser.parse_args()

    image_path = args.path

    if(image_path is None):
        print ('Please provide the path to image file. Try again.')
        exit(0)
    # degree = int(input("Enter degree: "))
    pwd = getpass.getpass("Enter password: ")
    encode(image_path, pwd)
    # (im,arr,saved_path)=encode(image_path, key_init(pwd))
    # efficiency_calc(image_path,im,arr, saved_path)
