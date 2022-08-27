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
def _enc_file(_file,secretKey,nonce):
    print(' encrypting file -----> {}'.format(_file))
    with open(_file,'rb') as _read:
        _data=_read.read()
    _aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    ciphertext, authTag = _aesCipher.encrypt_and_digest(_data)
    _d_cip_auth={}
    _d_cip_auth['cipher_text']=ciphertext
    _d_cip_auth['auth_tag']=authTag
    with open(_file,'wb') as _writ_r:
        pickle.dump(_d_cip_auth,_writ_r)
    print(' {} . -----> Encrypted'.format(_file))
def _fold(_,s,n):
    for __ in os.listdir(_):
        file_T(_+'/'+__,s,n)
def file_T(_file,s_key,nonce):
    if os.path.isfile(_file):
        print('{}  Is a File'.format(_file))
        _enc_file(_file,s_key,nonce)
    elif os.path.isdir(_file):
        print('{} is  directory'.format(_file))
        _fold(_file,s_key,nonce)
    else:
        print(" {} is a special file (socket, FIFO, device file)".format(_file))
    
    
def encrypt_AES_GCM(_file):
    secretkey,nonce=load_salt()
    print(secretkey)
    print(nonce)
    file_T(_file,secretkey,nonce)

_path='de'
encrypt_AES_GCM(_path)