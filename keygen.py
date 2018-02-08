import hashlib
import getpass
import binascii


def max_val(ht, wdth):
    return max(ht, wdth)

def keygen(psswd,H,W):
    # Encode the string into a byte array
    psswd_encoded = psswd.encode('utf-8')
    # Generate hash value
def p2b(text):
	word = ['{}'.format(bin(int(hashlib.sha256(text).hexdigest(), 16)))]
	print(word)           
    
    
p2b("goodboy")
    

    
