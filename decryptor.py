
from Crypto.Cipher import AES
import scrypt
import os
import binascii
import secrets
import pickle
def load_salt():
    with open('salt_data.bin','rb') as _bin:
        return f_salt(pickle.load(_bin))
def f_salt(_):
    secretKey=_['secret_key']
    nonce=_['aes_cipher']
    return (secretKey,nonce)
def _dec_file(_file,secretKey,nonce):
    print(' Decrypting File -----> '.format(_file))
    with open(_file,'rb') as _bin_r:
        _data_2=pickle.load(_bin_r)
    ciphertext=_data_2['cipher_text']  
    authTag=_data_2['auth_tag']
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    decrypt_ntext = aesCipher.decrypt_and_verify(ciphertext,authTag)
    with open(_file,'wb') as _bin_w:
        _bin_w.write(decrypt_ntext)
    print('{}  has Been Decrypted'.format(_file))
        
def _fold(_,s,n):
    for __ in os.listdir(_):
        file_T(_+'/'+__,s,n)
def file_T(_file,s_key,nonce):
    if os.path.isfile(_file):
        print(' {}  Is a  File '.format(_file))
        _dec_file(_file,s_key,nonce)
    elif os.path.isdir(_file):
        print(' {} is a directory '.format(_file))
        _fold(_file,s_key,nonce)
    else:
        print(" {} is a special file (socket, FIFO, device file)".format(_file))
    
def decrypt_AES_GCM(_file):
    secretkey,nonce=load_salt()
    print(secretkey)
    print(nonce)
    file_T(_file,secretkey,nonce)

_path='de'
decrypt_AES_GCM(_path)