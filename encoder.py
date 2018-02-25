from PIL import Image
from keygen import *
from utils import *
import argparse
import getpass



def automate_swap(arr, a, b):
    L = len(a)
    for i in range(L):
        temp = arr[a[i][0], a[i][1]]
        arr[a[i][0], a[i][1]] = arr[b[i][0], b[i][1]]
        arr[b[i][0], b[i][1]] = temp


def encode(image_path, TUPLE):
    extension=image_path.split('.')[-1]
    try:
        im = Image.open(image_path, "r")
    except FileNotFoundError:
        print ('Image path is incorrect. Try again.')
        exit(0)

    im = Image.open(image_path, "r")
    arr = im.load()  # pixel data stored in this 2D array
    (W, H) = im.size
    print(W, H)
    degree= int(0.36*W*H)

    tuple_a= TUPLE
    tuple_b= TUPLE

    for i in range(degree):
        tuple_a=tuple_b
        tuple_b= new_tuple(tuple_a)
        swap(arr, tuple_a, tuple_b)




    tokenized= image_path.split('.')
    saved_path= tokenized[0]+'_enc.'+tokenized[1]
    # im.show() #To display the image im
    im.save(saved_path)
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
    encode(image_path, key_init(pwd))
    # (im,arr,saved_path)=encode(image_path, key_init(pwd))
    # efficiency_calc(image_path,im,arr, saved_path)
