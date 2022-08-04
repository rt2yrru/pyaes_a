import random
def _rand_pass(length=100):
    _pwd=''
    for _ in range(0,length):

        random.seed()
        random.getstate()
        _c=chr(random.randrange(33,126))
        _pwd+=_c
    return _pwd
_ab=_rand_pass()
print(_ab)
with open('_pass.txt','w') as _fw:
    _fw.write(_ab)
    