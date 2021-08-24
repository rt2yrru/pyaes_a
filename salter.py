from Crypto.Cipher import AES
import scrypt
import os
import binascii
import secrets
import pickle
def salt_AES_GCM(password):
    _enc_data={}
    _enc_data['password']=password
    salt_length=1024*1024*5
    kdfSalt = secrets.token_bytes(salt_length)
    _enc_data['kdf_Salt']=kdfSalt

    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    _enc_data['secret_key']=secretKey
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    _enc_data['aes_cipher']=aesCipher.nonce
    with open('enc_data.bin','wb') as _bin:
        pickle.dump(_enc_data,_bin)
    print('Salting Complete')

password = b's3kr3tp4ssw0rd'

print('Salting:')
_enc_d=salt_AES_GCM(password)
