import hashlib
import getpass
import binascii
import math


def max_val(ht, wdth):
    return max(ht, wdth)
	
def keygen(psswd,H,W):
    word = ['{}'.format(bin(int(hashlib.sha256(psswd.encode('utf-8')).hexdigest(), 16)))]
    print(word)
    h_bit= int(math.ceil(math.log(H)/math.log(2)))
    w_bit= int(math.ceil(math.log(W)/math.log(2)))
    B= h_bit + w_bit
    print(B, h_bit, w_bit)
    bin_hash= str(word)[4:-2]
    chunks = [(bin_hash[i:i+B]) for i in range(0,len(bin_hash),B)]
    print(chunks)
    init_tuple = [c for c in chunks if len(c)==B]
    init_tuple = [(c[0:w_bit],c[h_bit:w_bit+h_bit]) for c in init_tuple]
    print(init_tuple)
    
def xnor(a,b):
	return (str(bin(~(a ^ b)))).zfill(10)
	#abrupt truncation

print(xnor(150,123))
#keygen("goodboy", 3840, 2160)
