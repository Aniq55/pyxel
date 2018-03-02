import numpy as np
import matplotlib.pyplot as plt
from keygen import *
from encoder import *
from decoder import *
from img_sim import similarity_index

# Image necrypted by key K1 is decrypted with key K2
# K1 and K2 have only one number different in the key tuple
# This will measure the chaos of the proposed crypto-system

original_seed = encode('testimg/emma.png', "goodboy")
print(original_seed)
corrupted_seed = original_seed
x1= corrupted_seed[len(corrupted_seed)-1][0]
x2= corrupted_seed[len(corrupted_seed)-1][1]
# slight change in only one value
corrupted_seed[len(corrupted_seed)-1]= (abs(x1-2),x2)
print(corrupted_seed)
corrupted_seed2= decode('testimg/emma_enc.png', "goodboy", corrupted_seed)

similarity_index('testimg/emma.png', 'testimg/emma_enc_dec.png')
