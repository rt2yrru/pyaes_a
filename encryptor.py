from Crypto.Cipher import AES
import scrypt
import os
import binascii
import secrets
import pickle
    
def encrypt_AES_GCM(_file):
    with open('salt_data.bin','rb') as _bin:
        _enc_k=pickle.load(_bin)

    secretKey=_enc_k['secret_key']
    nonce=_enc_k['aes_cipher']
    print(secretKey)

    if os.path.isdir(_file): 
        print("It is a directory")  
        print(' doing Fdr Loop')
        for r, d, f in os.walk(_file):
            for file in f:
                _path=os.path.join(_file, file)
                with open(_path,'rb') as _read:
                    _data=_read.read()
                _aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
                ciphertext, authTag = _aesCipher.encrypt_and_digest(_data)
                _d_cip_auth={}
                _d_cip_auth['cipher_text']=ciphertext
                _d_cip_auth['auth_tag']=authTag
                with open(_path,'wb') as _writ_r:
                    pickle.dump(_d_cip_auth,_writ_r)
                print(' {} . -----> Encrypted'.format(_path))
    elif os.path.isfile(_file):  
        print("\nIt is a file") 
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
    else:  
        print("It is a special file (socket, FIFO, device file)" )
    
_file='g'
_enc_d=encrypt_AES_GCM(_file)
#print('file Encrypted')

    #
    
#aesCipher = AES.new(secretKey, AES.MODE_GCM)
   # _enc_data['aes_cipher']=aesCipher.nonce
    #_enc_data['aes_Cipher']=aesCipher


#ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
#    _enc_data['auth_Tag']=authTag
 #   with open(_file,'wb') as _bin_w:
#        _bin_w.write(ciphertext)
#    return _enc_data
