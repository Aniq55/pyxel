import hashlib
import getpass
import binascii
import math


def key_init(psswd,H,W):
    word = ['{}'.format(bin(int(hashlib.sha256(psswd.encode('utf-8')).hexdigest(), 16)))]
    # print(word)
    h_bit= int(math.ceil(math.log(H)/math.log(2)))
    w_bit= int(math.ceil(math.log(W)/math.log(2)))
    B= h_bit + w_bit
    # print(B, h_bit, w_bit)
    bin_hash= str(word)[4:-2]
    chunks = [(bin_hash[i:i+B]) for i in range(0,len(bin_hash),B)]
    # print(chunks)
    init_tuple = [c for c in chunks if len(c)==B]
    init_tuple = [ ( int(c[0:w_bit][2:],2),int(c[h_bit:w_bit+h_bit][2:],2) ) for c in init_tuple]
    return init_tuple

def xnor(a,b):
    return abs(~(a^b))

# Function to generate the next sequence of tuples
def next_tuple(tuple):
    i=0
    new_tuple=[]
    while i<len(tuple)-1:
        a= xnor(tuple[i][0],tuple[i+1][0])
        b= xnor(tuple[i][1],tuple[i+1][1])
        new_tuple.append((a,b))
        i=i+1
    a= xnor(tuple[i][0],tuple[0][0])
    b= xnor(tuple[i][1],tuple[0][1])
    new_tuple.append((a,b))
    return new_tuple

def all_keys(init_tuple, degree):
    key=[]
    this_tuple= init_tuple
    key.append(this_tuple)
    for i in range(degree):
        this_tuple= next_tuple(this_tuple)
        key.append(this_tuple)
    return key

# print(xnor(5,100))
# TUPLE= key_init("goodboy", 3840, 2160)
# print(all_keys(TUPLE, 5))

# print(len(TUPLE))
# print(len(next_tuple(TUPLE)))
