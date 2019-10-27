import string
def check(pwd):
    if not isinstance(pwd,str) or len(pwd) < 6:
        return 'not suitable for password'
    d = {1:'week',2:'below middle',3:'above middle',4:'strong'}
    r = [False]*4
    for ch in pwd:
        if not r[0] and ch in string.digits:
            r[0] = True
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        elif not r[3] and ch in ',.!;?<>':
            r[3] = True
    return d.get(r.count(True),'error')
print(check('a2Cd,'))
