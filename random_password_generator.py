import secrets
print(secrets.SystemRandom())
_b=secrets.token_bytes(256*4)
print(_b)
print(type(_b))
print(len(_b))
with open('_pass.bin','wb') as _w_b:
    _w_b.write(_b)
    
