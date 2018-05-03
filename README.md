# RSA-Detail
涉及rsa算法的加解密

项目实现原理
![Image text](https://github.com/Amoswish/RSA-Detail/blob/master/rsa.png)
具体在p,q中我采取随机数产生2^8~2^16的随机数，然后采取miller-radio进行10次素数检测，如下所示：

![Image text](https://github.com/Amoswish/RSA-Detail/blob/master/rsa1.png)


然后利用扩展欧几里得算法求出同余方程，再根据同余方程找到e的模反元素d从而进行加解密，在加密过程中我采取每两位为一个加密单元



主要特点	

  利用miller-radio算法进行素数检测和利用扩展欧几里得算法求出一阶同余方程后求解出e的模反元素d从而达到加密的素数以及公钥和密钥
主要问题及改进思路	

  界面不够美观。针对加密时加密后的密文必须用字符串记录，否则被n mod后的数的大小未知，所以如果改进的话应该利用hash函数将密文映射为同一长度，这样应该可以解决上述问题
