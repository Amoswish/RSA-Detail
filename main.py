import random
# 快速积取模 a*b%n
def fastMulMod(a, b, n):
    ans = 0;
    while (b):
        if (b & 1):
            ans = (ans + a) % n;
            a = (a + a) % n;
            b >>= 1;
    return ans;
# 快速幂取模 a^b % c
def fastExpMod(a, b, c):
    a=a%c
    ans=1
    #这里我们不需要考虑b<0，因为分数没有取模运算
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans
# Miller - Rabin素数检测算法
def miller_rabin(n):
    s = 10
    #i, j, a, x, y, t, u,
    if (n == 2):
        return 1
    if ((n < 2) or (not(n & 1))):
        return 0;
    #for (t=0, u=n-1;!(u & 1);t++, u >>= 1) # n-1=u * 2 ^ t
    t = 0
    while(1):
        u = n - 1
        u >>= 1
        t = t+1
        if(not(u & 1)):
            break
    for i in range(s):
        a = random.rand()%(n-1)+1
        x = fastExpMod(a, u, n)
        for j in range(t):
            y = fastMulMod(x, x, n)
            if (y == 1 and x != 1 and x != n - 1):
                return 0
            x = y
        if (x != 1):
            return 0
    return 1

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
    if b == 0:
        return (a, 1, 0)
    d, x, y = extendGcd(b, a%b)
    return (d, y, x-a//b*y)
def mod_linear_equation(a, b, n):
    # ax === b (mod n)
    d, x, y = extendGcd(a, n)
    if b % d:
        raise 'no solution'
    x0 = x * (b // d) % n
    # 特解
    # 通解：
    # [(x0+i*(n//d))%n for i in range(d)]
    return d, x0
#加密 需 e n
def encryptionRSA(n,e,cleartext):
    ct = cleartext.upper()#将其转化为大写
    #ciphertext =[['' for i in range(2)] for i in range(100)]
    ctlen = len(cleartext)
    ciphertext = ['' for i in range(int(ctlen/2))]
    num = 0
    tempi = 0
    while(1):
        #针对字符串中每两个字符进行加密
        tempct1 =ord( ct[num] )#获取第一个字符
        tempct2 =ord( ct[num+1] )#获取第二个字符
        tempct3 = tempct2 + tempct1*100#转化成数字
        print(tempct3,e,n)
        tempciphertext = fastExpMod(tempct3,e,n)
        #tempciphertext = fastExpMod(3, 5, 6)
        print(tempciphertext)
        ciphertext[tempi] = tempciphertext
        tempi = tempi + 1
        num = num + 2
        if(num >= ctlen):
            break
    print( ciphertext[0:int(ctlen/2)])
    return ciphertext
#解密 需 d n
def decryptionRSA(n,d,ciphertext):
    cleartext = ""
    for num in range(len(ciphertext)):
        tempclt1 = int(ciphertext[num])
        tempcleartext = fastExpMod(tempclt1, d, n)
        tempclt12 = tempcleartext // 100
        tempclt13 = tempcleartext - (tempcleartext // 100)*100
        cleartext = cleartext + chr(tempclt12)#解密后的第一个字符
        cleartext = cleartext + chr(tempclt13)#解密后的第二个字符
    return cleartext
def calculate_key():
    while(1):
        p = random.randint(256, 65535) # 2^8< p < 2^16
        q = random.randint(256, 65535) # 2^8< q < 2^16
        print(p,q)
        print(miller_rabin(p))
        if ( (p != q) and(miller_rabin(p) == 1 )and (miller_rabin(p) == 1) ):
            break
    n = p * q
    fai = (p-1)*(q-1)
    #求与fai互质的e
    e = random.randint(1,n-1)
    while(1):
        if(Coprime(e,fai)==1):break
        else: e = random.randint(1, n-1)
    (x,y) = mod_linear_equation(e,1,fai)#从x,y中任意选一个即为d
    d = abs(y)
    return (n,e,d);
def main():
    (n, e, d) = calculate_key()
    cleartext = input("请输入需要加密的明文")
    ciphertext = encryptionRSA(n,e,cleartext)
    print("密文为",ciphertext[0:len(ciphertext)])
    finallcleartext = decryptionRSA(n, d, ciphertext)
    print("明文为" + finallcleartext)
if __name__ == '__main__':
    print(miller_rabin(3))
    #main()
