from random import choice,randint
import string
import codecs
StringBase = '\u7684\u4e00\u4e86\u662f\u6211\u4e0d\u5728\u4eba'
def getEmail():
    suffix = ['.com','.org','.net','.cn']
    characters = string.ascii_letters+string.digits+'_'
    username = ''.join((choice(characters) for i in range(randint(6,12))))
    domain = ''.join((choice(characters) for i in range(randint(3,6))))
    return username+'@'+domain+choice(suffix)
def getTelNo():
    return ''.join((str(randint(0,9)) for i in range(11)))
def getNameOrAddress(flag):
    if flag==1:
        rangestart,rangeend=2,5
    elif flag==0:
        rangestart,rangeend=10,30
    result = ''.join((choice(StringBase) for i in range(randint(rangestart,rangeend))))
    return result
def getSex():
    return choice(('ÄÐ','Å®'))
def getAge():
    return str(randint(18,100))
def main(filename):
    with codecs.open(filename,'w','utf-8') as fp:
        fp.write('Name,Sex,Age,TelNo,Address,Email\n')
        for i in range(200):
            name = getNameOrAddress(1)
            sex = getSex()
            age = getAge()
            tel = getTelNo()
            address = getNameOrAddress(0)
            email = getEmail()
            line = ','.join([name,sex,age,tel,address,email])+'\n'
            fp.write(line)
def output(filename):
    with codecs.open(filename,'r','utf-8') as fp:
        for line in fp:
            line = line.split(',')
            for i in line:
                print(i,end=',')
            print()
if __name__=='__main__':
    filename = 'information.txt'
    main(filename)
    output(filename)