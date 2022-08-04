from Crypto.Cipher import AES
import scrypt
import os
import binascii
import secrets
import pickle
with open('salt_data.bin','rb') as _bin:
    _data=pickle.load(_bin)
def decrypt_AES_GCM(_file):
   # (kdfSalt, nonce) = encryptedMsg
    with open(_file,'rb') as _bin_r:
        _data_2=pickle.load(_bin_r)
    ciphertext=_data_2['cipher_text']  
    authTag=_data_2['auth_tag']
    
    secretKey=_data['secret_key']
    nonce=_data['aes_cipher']
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext,authTag)
    with open(_file,'wb') as _bin_w:
        _bin_w.write(plaintext)
    return ' Decrypted'


_file='_g'
if os.path.isdir(_file): 
    print("It is a directory")  
    print(' doing Fdr Loop')
    for r, d, f in os.walk(_file):
        for file in f:
            _path=r+'/'+file
            decryptedMsg = decrypt_AES_GCM(_path)
            print('{}  has Been Decrypted'.format(_path))
elif os.path.isfile(_file): 
    decryptedMsg = decrypt_AES_GCM(_file)
    print('{}  has Been Decrypted'.format(_file))
else:
    print(' special File')