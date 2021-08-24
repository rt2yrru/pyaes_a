from Crypto.Cipher import AES
import scrypt, os, binascii
import secrets
import pickle
with open('enc_data.bin','rb') as _bin:
    _data=pickle.load(_bin)
def decrypt_AES_GCM(_file,encryptedMsg, password):
    (kdfSalt, nonce) = encryptedMsg
    with open(_file,'rb') as _bin_r:
        _data_2=pickle.load(_bin_r)
    ciphertext=_data_2['cipher_text']  
    authTag=_data_2['auth_tag']
    secretKey = scrypt.hash(password, kdfSalt, N=16384, r=8, p=1, buflen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext,authTag)
    with open(_file,'wb') as _bin_w:
        _bin_w.write(plaintext)
    return plaintext

#kdfSalt, ciphertext, aesCipher.nonce, authTag)
#decryptedMsg = decrypt_AES_GCM(encryptedMsg,_data['password'])
#print("decryptedMsg", decryptedMsg)
_file='g'
#_datum=(_data['kdf_Salt'],_data['aes_cipher'],_data['auth_Tag'])
_datum=(_data['kdf_Salt'],_data['aes_cipher'])
if os.path.isdir(_file): 
    print("It is a directory")  
    print(' doing Fdr Loop')
    for _ in os.listdir(_file):
        _path=_file+'/'+_
        decryptedMsg = decrypt_AES_GCM(_path,_datum,_data['password'])
        print('{}  has Been Decrypted'.format(_))
elif os.path.isfile(_file): 
    decryptedMsg = decrypt_AES_GCM(_file,_datum,_data['password'])
    print('{}  has Been Decrypted'.format(_file))
else:
    print(' special File')