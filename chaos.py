import numpy as np
import matplotlib.pyplot as plt
from keygen import *
from encoder import *
from decoder import *
from img_sim import *

# measurement in the change in encrypted image by a small change in init tuple
# same thing done during decryption
# Image necrypted by key K1 is decrypted with key K2
# K1 and K2 have only one number different in the key tuple
# This will measure the chaos of the proposed crypto-system

original_seed = encoder('emma.png', "goodboy")
# A = get the latest image
corrupted_seed = original_seed
x= corrupted_seed[len(corrupted_seed)-1]
# slight change in only one value
corrupted_seed[len(corrupted_seed)-1]= abs(x-2)
corrupted_seed2= encoder('emma.png', "goodboy", corrupted_seed)
# B = get the latest image

# S= similarity_index(A, B)
