import random
# 快速幂取模 a^b%n
def ModeExp(a,b,n):
    ans = 1
    a= a % n
    while(b>0):
        if(b%2 == 1):
            ans = (ans*a) % n
            b = b/2
            a= (a*a) % n
    return ans
#判断两数是否互质
def Coprime(m,n):
    d1=d2=d3=1
    if(m <= n):
        d1 = m
        d2 = n
    else:
        d1 = n
        d2 = m
    while(d3!=0):
        d3 = d2 % d1
        d2 = d1
        d1 = d3
    if(d2 == 1): return 1 #代表m,n互质
    else: return 0
# 辗转相除法
def gcd(a,b):
    while(a!=b):
        if(a>b): a-=b
        else: b-=a
    return a
#扩展欧几里得算法
def extendGcd(a,b):
    if(b == 0):
        return (1,0,a)
    (x,y,r) = extendGcd(b,a%b)
    t = y
    y = x - int(a/b) *y
    x = t
    return (x, y, r)
#加密 需 e n
def encryptionRSA(n,e,cleartext):
    ct = cleartext.upper()#将其转化为大写
    ciphertext = ''
    for num in len(ct):
        #针对字符串中每两个字符进行加密
        tempct1 =int( ct[num] )#获取第一个字符
        tempct2 =int( ct[num+1] )#获取第二个字符
        tempct3 = tempct2 + tempct1*100#转化成数字
        tempciphertext = ModeExp(tempct3,e,n)
        ciphertext = ciphertext+chr(tempciphertext)
        num = num + 1
    return ciphertext
#解密 需 d n
def decryptionRSA(n,d,ciphertext):
    cleartext = ""
    for num in len(ciphertext):
        tempclt1 = int(ciphertext[num])
        tempcleartext = ModeExp(tempclt1, d, n)
        tempclt12 = int(tempcleartext / 100)
        tempclt13 = int(tempcleartext - int(tempcleartext / 100)*100)
        cleartext = cleartext + chr(tempclt12)#解密后的第一个字符
        cleartext = cleartext + chr(tempclt13)#解密后的第二个字符
    return ciphertext
def calculate_key():
    p = 100003
    q = 200007
    n = p * q
    fai = (p-1)*(q-1)
    #求与fai互质的e
    e = random.randint(1,n)
    while(1):
        if(Coprime(e,fai)==1):break
        else: e = random.randint(1, n)
    (x,y,r) = extendGcd(e,fai)#从x,y中任意选一个即为d
    print(x,y,r)
    d = abs(x)
    return (n,e,d);
def main():
    (n, e, d) = calculate_key()
    cleartext = input("请输入需要加密的明文")
    ciphertext = encryptionRSA(n,e,cleartext)
    print("密文为"+ciphertext)
    finallcleartext = decryptionRSA(n, d, ciphertext)
    print("明文为" + finallcleartext)
if __name__ == '__main__':
    main()